from repository.driver_repository import DriverRepository
from repository.location_repository import LocationRepository
from repository.road_repository import RoadRepository
from models.user import User
from services.matching_service import MatchingService
from services.navigation_service import NavigationService
from services.trip_analytics_service import TripAnalyticsService


class RideService:
    
    def __init__(self):
        self.matching_service = MatchingService()
        self.navigation_service = NavigationService()
        self.trip_analytics_service = TripAnalyticsService()
        self.driver_repository = DriverRepository()
        self.location_repository = LocationRepository()
        self.road_repository = RoadRepository()
    
    
    def book_ride(
    self,
    pickup,
    destination,
    passenger,
    drivers,
    graph
):
        driver_options = self.matching_service.rank_drivers(
            passenger,
            drivers
        )

        best_driver = None
        score = 0

        if driver_options:
            best_driver = driver_options[0]["driver"]
            score = driver_options[0]["score"]
        
        distance, path = self.navigation_service.find_shortest_path(
            graph,
            pickup,
            destination
        )

        vehicle = best_driver.vehicle if best_driver else None
        trip_prediction = self.trip_analytics_service.predict_trip(
            distance,
            vehicle
        )

        return {

        "driver": best_driver,

        "distance": distance,

        "path": path,
        
        "score":score,

        "driver_options": driver_options

        ,"trip_prediction": trip_prediction

    }
