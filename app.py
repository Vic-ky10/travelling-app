from flask import Flask, render_template, request

from models.user import User

from repository.driver_repository import DriverRepository
from repository.location_repository import LocationRepository
from repository.road_repository import RoadRepository


from services.ride_service import RideService



app = Flask(__name__)
 


driver_repository = DriverRepository()                     
location_repository = LocationRepository()                
road_repository = RoadRepository()
ride_service = RideService()

     

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
    
   
    

    return render_template(
        "result.html",
        driver = ride["driver"],
        pickup= pickup,
        destination = destination,
        distance=ride["distance"],
        path=ride["path"],
        score=ride["score"],
    )

if __name__ == "__main__":
    app.run(debug=True)