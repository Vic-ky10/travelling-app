from flask import Flask, render_template, request
from models.driver import Driver
from models.vehicle import Vehicle
from services.matching_service import MatchingService
from repository.driver_repository import DriverRepository
from repository.location_repository import LocationRepository
from models.user import User
from repository.road_repository import RoadRepository
from services.navigation_service import NavigationService



app = Flask(__name__)


matching_service = MatchingService()
driver_repository = DriverRepository()                     
location_repository = LocationRepository()                
road_repository = RoadRepository()
navigation_service = NavigationService()        

@app.route("/")
def home():
    locations = list(
    location_repository.get_all_locations().keys()
)
    
    return render_template(
        "home.html",
        locations = locations
    )


@app.route("/find-driver", methods=["POST"])
def find_driver():

    pickup = request.form["pickup"]
    destination = request.form["destination"]
    graph = road_repository.get_graph()
    
    distance, path = navigation_service.find_shortest_path(
        graph,
        pickup,
        destination
    )
    
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
    best_driver = matching_service.find_best_driver(passenger,drivers)
    
   
    

    return render_template(
        "result.html",
        driver=best_driver,
        pickup= pickup,
        destination = destination,
        distance= distance
    )

if __name__ == "__main__":
    app.run(debug=True)