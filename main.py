from models.user import User
from models.vehicle import Vehicle
from models.driver import Driver
from models.ride import Ride
from services.matching_service import MatchingService
from services.tracking_service import Trackingservice
from data.graph import graph
from services.navigation_service import NavigationService
user = User(
    101,
    "Vicky",
    13.0827,
    80.2707
)

vehicle = Vehicle(
    "TN10AB1234",
    "Hyundai",
    "i20",
    "White",
    "Car"
)
driver = Driver(
   102,
   "rahul",
   13.234,
   80.3244,
   vehicle,
   5.0,
   True
)
ride = Ride(
    1,
    user,
    driver,
    "Tambaram",
    "T Nagar"
)

user.update_location(
     13.1000,
    80.3000
)
print("=== User===")
user.display_info()



print("\n===Driver===")
driver.display_driver_info()


print("\n=== Ride Created ===")
ride.display_ride()

ride.start_ride()

print("\n=== Ride Started ===")
ride.display_ride()

ride.complete_ride()

print("\n=== Ride Completed ===")
ride.display_ride()


vehicle1 = Vehicle("TN01AA1111", "Hyundai", "i20", "White", "Car")
vehicle2 = Vehicle("TN02BB2222", "Honda", "City", "Black", "Car")
vehicle3 = Vehicle("TN03CC3333", "Suzuki", "Swift", "Red", "Car")

driver1 = Driver(201, "Rahul", 13.0, 80.0, vehicle1, 4.7)
driver2 = Driver(202, "Arjun", 13.1, 80.2, vehicle2, 4.9, False)
driver3 = Driver(203, "Vicky", 13.2, 80.1, vehicle3, 5.0)

drivers = [driver1, driver2, driver3]


from services.matching_service import MatchingService

MatchingService = MatchingService()

best_driver = MatchingService.find_best_driver(drivers)
print("\n Best Driver Selected")


tracking_service = Trackingservice()

tracking_service.move_driver(
    driver,
    13.050,
    80.100
)

driver.display_driver_info()


from services.ride_service import Rideservice

ride_service = Rideservice()

ride = ride_service.book_ride(
    passenger=user,
    drivers= drivers,
    pickup="Tambaram",
    drop="T Nagar"
)

ride.display_ride()



navigation_service = NavigationService()

distance, path = navigation_service.find_shortest_path(
    graph,
    "Home",
    "Office"
)

print(f"Shortest Distance : { distance} km ")
print("Route :","-> ".join(path))