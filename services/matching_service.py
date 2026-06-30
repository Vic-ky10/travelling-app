

class MatchingService:

    def calculate_driver_features(self, driver, passenger):

        pickup_distance = (
            (driver.latitude - passenger.latitude) ** 2 +
            (driver.longitude - passenger.longitude) ** 2
        ) ** 0.5

        distance_score = max(1, 10 - (pickup_distance * 20))
        rating_score = driver.rating * 2
        availability_score = 10 if driver.is_available else 0
        vehicle_score = 8

        if driver.vehicle.vehicle_type == "SUV":
            vehicle_score = 8.5

        if driver.vehicle.vehicle_type == "Premium":
            vehicle_score = 9

        return {
            "pickup_distance": pickup_distance,
            "distance_score": distance_score,
            "rating_score": rating_score,
            "availability_score": availability_score,
            "vehicle_score": vehicle_score
        }

    def predict_match_score(self, features):

        score = (
            (features["distance_score"] * 0.55) +
            (features["rating_score"] * 0.25) +
            (features["availability_score"] * 0.15) +
            (features["vehicle_score"] * 0.05)
        )

        return max(1, min(score, 10))

    def build_recommendation_reasons(self, driver, features):

        reasons = []

        if features["pickup_distance"] <= 0.1:
            reasons.append("very close to pickup")
        elif features["pickup_distance"] <= 0.25:
            reasons.append("near pickup")
        else:
            reasons.append("available for this route")

        if driver.rating >= 4.8:
            reasons.append("high rating")

        if features["availability_score"] == 10:
            reasons.append("available now")

        return reasons

    def rank_drivers(self, passenger, drivers):

        ranked_drivers = []

        for driver in drivers:

            if not driver.is_available:
                continue

            features = self.calculate_driver_features(
                driver,
                passenger
            )
            score = self.predict_match_score(features)
            reasons = self.build_recommendation_reasons(
                driver,
                features
            )

            ranked_drivers.append({
                "driver": driver,
                "score": round(score, 2),
                "pickup_distance": round(features["pickup_distance"], 2),
                "feature_scores": {
                    "distance": round(features["distance_score"], 2),
                    "rating": round(features["rating_score"], 2),
                    "availability": round(features["availability_score"], 2),
                    "vehicle": round(features["vehicle_score"], 2)
                },
                "reasons": reasons
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
    
    
