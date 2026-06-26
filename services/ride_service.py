from repository.driver_repository import DriverRepository
from repository.location_repository import LocationRepository
from repository.road_repository import RoadRepository
from models.user import User
from services.matching_service import MatchingService
from services.navigation_service import NavigationService


class RideService:
    
    def __init__(self):
        self.matching_service = MatchingService()
        self.navigation_service = NavigationService()
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
        best_driver,score = self.matching_service.find_best_driver(
            passenger,
            drivers
        )
        
        distance, path = self.navigation_service.find_shortest_path(
            graph,
            pickup,
            destination
        )

        return {

        "driver": best_driver,

        "distance": distance,

        "path": path,
        
        "score":score

    }