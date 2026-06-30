class TripAnalyticsService:

    def predict_trip(self, distance, vehicle=None):

        traffic_level = self.get_traffic_level(distance)
        traffic_multiplier = self.get_traffic_multiplier(traffic_level)
        vehicle_multiplier = self.get_vehicle_multiplier(vehicle)

        base_fare = 50
        per_km_rate = 18
        fare = (base_fare + (distance * per_km_rate)) * traffic_multiplier
        fare = fare * vehicle_multiplier

        trip_minutes = max(3, round(distance * self.get_minutes_per_km(traffic_level)))

        return {
            "fare": round(fare),
            "trip_minutes": trip_minutes,
            "traffic_level": traffic_level,
            "price_reason": self.build_price_reason(
                distance,
                traffic_level,
                vehicle_multiplier
            )
        }

    def get_traffic_level(self, distance):

        if distance <= 3:
            return "Low"

        if distance <= 6:
            return "Medium"

        return "High"

    def get_traffic_multiplier(self, traffic_level):

        if traffic_level == "High":
            return 1.35

        if traffic_level == "Medium":
            return 1.15

        return 1.0

    def get_vehicle_multiplier(self, vehicle):

        if vehicle is None:
            return 1.0

        if vehicle.vehicle_type == "SUV":
            return 1.2

        if vehicle.vehicle_type == "Premium":
            return 1.35

        return 1.0

    def get_minutes_per_km(self, traffic_level):

        if traffic_level == "High":
            return 4

        if traffic_level == "Medium":
            return 3

        return 2

    def build_price_reason(self, distance, traffic_level, vehicle_multiplier):

        reason = f"{distance} km route + {traffic_level.lower()} traffic"

        if vehicle_multiplier > 1:
            reason += " + vehicle type"

        return reason
