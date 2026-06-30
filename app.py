from flask import Flask, render_template, request

from models.user import User

from repository.driver_repository import DriverRepository
from repository.location_repository import LocationRepository
from repository.road_repository import RoadRepository


from services.ride_service import RideService
from services.map_service import MapService



app = Flask(__name__)
 


driver_repository = DriverRepository()                     
location_repository = LocationRepository()                
road_repository = RoadRepository()
ride_service = RideService()
map_service = MapService()

     

@app.route("/")
def home():
    locations = list(
    location_repository.get_all_locations().keys()
)
    map_data = map_service.build_city_map(
        location_repository.get_all_locations(),
        road_repository.get_graph()
    )
    
    return render_template(
        "home.html",
        locations = locations,
        map_data = map_data
    )


@app.route("/find-driver", methods=["POST"])
def find_driver():

    pickup = request.form["pickup"]
    destination = request.form["destination"]
    graph = road_repository.get_graph()
    
    
    
    drivers = driver_repository.get_all_drivers()
   
    location_data = location_repository.get_all_locations()
    pickup_latitude = location_data[pickup][0]
    pickup_longitude = location_data[pickup][1]
    passenger = User(
        1, 
        "Vicky",
        pickup_latitude,
        pickup_longitude
    )
    
    ride = ride_service.book_ride(
        pickup,
        destination,
        passenger,
        drivers,
        graph
    )

    if ride["driver"] is None:
        return "No available drivers found", 404
    
   
    

    return render_template(
        "result.html",
        driver = ride["driver"],
        driver_options = ride["driver_options"],
        pickup= pickup,
        destination = destination,
        distance=ride["distance"],
        path=ride["path"],
        score=ride["score"],
        trip_prediction=ride["trip_prediction"],
    )


@app.route("/choose-driver", methods=["POST"])
def choose_driver():

    pickup = request.form["pickup"]
    destination = request.form["destination"]
    driver_id = int(request.form["driver_id"])

    drivers = driver_repository.get_all_drivers()
    selected_driver = None

    for driver in drivers:
        if driver.user_id == driver_id:
            selected_driver = driver
            break

    if selected_driver is None:
        return "Driver not found", 404

    graph = road_repository.get_graph()
    location_data = location_repository.get_all_locations()
    pickup_latitude = location_data[pickup][0]
    pickup_longitude = location_data[pickup][1]

    passenger = User(
        1,
        "Vicky",
        pickup_latitude,
        pickup_longitude
    )

    driver_options = ride_service.matching_service.rank_drivers(
        passenger,
        drivers
    )

    selected_score = 0
    pickup_distance = 0

    for driver_option in driver_options:
        if driver_option["driver"].user_id == driver_id:
            selected_score = driver_option["score"]
            pickup_distance = driver_option["pickup_distance"]
            break

    distance, path = ride_service.navigation_service.find_shortest_path(
        graph,
        pickup,
        destination
    )

    trip_prediction = ride_service.trip_analytics_service.predict_trip(
        distance,
        selected_driver.vehicle
    )

    tracking_duration = max(5, min(int(pickup_distance * 80) + 5, 20))
    arrival_minutes = max(1, round(pickup_distance * 20))

    return render_template(
        "booking.html",
        driver=selected_driver,
        pickup=pickup,
        destination=destination,
        distance=distance,
        path=path,
        score=selected_score,
        pickup_distance=pickup_distance,
        tracking_duration=tracking_duration,
        arrival_minutes=arrival_minutes,
        trip_prediction=trip_prediction
    )


@app.route("/start-trip", methods=["POST"])
def start_trip():

    pickup = request.form["pickup"]
    destination = request.form["destination"]
    driver_id = int(request.form["driver_id"])

    drivers = driver_repository.get_all_drivers()
    selected_driver = None

    for driver in drivers:
        if driver.user_id == driver_id:
            selected_driver = driver
            break

    if selected_driver is None:
        return "Driver not found", 404

    graph = road_repository.get_graph()
    distance, path = ride_service.navigation_service.find_shortest_path(
        graph,
        pickup,
        destination
    )
    trip_prediction = ride_service.trip_analytics_service.predict_trip(
        distance,
        selected_driver.vehicle
    )
    trip_duration = max(7, min(int(distance * 2), 30))

    return render_template(
        "trip.html",
        driver=selected_driver,
        pickup=pickup,
        destination=destination,
        distance=distance,
        path=path,
        trip_prediction=trip_prediction,
        trip_duration=trip_duration,
        route_map=map_service.build_route_map(
            location_repository.get_all_locations(),
            path
        )
    )

if __name__ == "__main__":
    app.run(debug=True)
