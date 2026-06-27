

class MatchingService:

    def rank_drivers(self, passenger, drivers):

        ranked_drivers = []

        for driver in drivers:

            if not driver.is_available:
                continue

            pickup_distance = (
                (driver.latitude - passenger.latitude) ** 2 +
                (driver.longitude - passenger.longitude) ** 2
            ) ** 0.5

            distance_score = max(1, 10 - (pickup_distance * 20))
            rating_score = driver.rating * 2
            score = (distance_score * 0.8) + (rating_score * 0.2)
            score = max(1, min(score, 10))

            ranked_drivers.append({
                "driver": driver,
                "score": round(score, 2),
                "pickup_distance": round(pickup_distance, 2)
            })

        ranked_drivers.sort(
            key=lambda driver_option: driver_option["score"],
            reverse=True
        )

        return ranked_drivers

    def find_best_driver(self, passenger, drivers):

        ranked_drivers = self.rank_drivers(passenger, drivers)

        if not ranked_drivers:
            return None, 0

        best_option = ranked_drivers[0]

        return best_option["driver"], best_option["score"]     
    
    
