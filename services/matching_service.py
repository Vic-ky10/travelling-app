

class MatchingService:

    def find_best_driver(self, passenger, drivers):

        best_driver = None
        best_score = float("-inf")

        for driver in drivers:

            if not driver.is_available:
                continue

            distance = (
                (driver.latitude - passenger.latitude) ** 2 +
                (driver.longitude - passenger.longitude) ** 2
            ) ** 0.5

            score = (driver.rating * 10) - distance

            if score > best_score:

                best_score = score
                best_driver = driver

        return best_driver,round(best_score,2)     
    
    