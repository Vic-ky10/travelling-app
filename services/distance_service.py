import math

class DistanceService:
    def calculate_distance(self, user, driver):
        
        x= driver.latitude - user.latitude
        y= driver.longitude - user.longitude
        
        distance = math.sqrt( x ** 2 + y ** 2)  # euclidean distance
        return distance
    