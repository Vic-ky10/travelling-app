from models.user import User


class Driver(User):

    def __init__(
        self,
        user_id,
        name,
        latitude,
        longitude,
        vehicle,
        rating=5.0,
        is_available=True
    ):

        super().__init__(
            user_id,
            name,
            latitude,
            longitude
        )

        self.vehicle = vehicle
        self.rating = rating
        self.is_available = is_available

    def display_driver_info(self):

        print(f"Driver ID   : {self.user_id}")
        print(f"Name        : {self.name}")
        print(f"Rating      : {self.rating}")
        print(f"Available   : {self.is_available}")

   
        print("\n===vehicle Information===")
        self.vehicle.display_info()