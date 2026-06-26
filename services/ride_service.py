from models.ride import Ride
from services.matching_service import MatchingService


class Rideservice:
    
    def __init__(self):
        self.matching_service = MatchingService()
    
    def book_ride(
        self,
        passenger,
        drivers,
        pickup,
        drop
    ):
        driver = self.matching_service.find_best_driver(
            drivers
        )    
        
        ride = Ride(
            1,
            passenger,
            driver,
            pickup,
            drop
        )
        return ride