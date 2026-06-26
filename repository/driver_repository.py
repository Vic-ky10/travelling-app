from models.driver import Driver
from models.vehicle import Vehicle


class DriverRepository:

    def get_all_drivers(self):

        driver1 = Driver(
            101,
            "Rahul",
            13.10,
            80.20,
            Vehicle(
                "TN10AB1234",
                "Hyundai",
                "i20",
                "White",
                "Car"
            ),
            4.9
        )

        driver2 = Driver(
            102,
            "Arun",
            13.20,
            80.25,
            Vehicle(
                "TN20CD5678",
                "Honda",
                "City",
                "Black",
                "Car"
            ),
            4.7
        )

        driver3 = Driver(
            103,
            "Karthik",
            13.05,
            80.10,
            Vehicle(
                "TN30EF8888",
                "Suzuki",
                "Swift",
                "Red",
                "Car"
            ),
            4.8
        )

        driver4 = Driver(
            104,
            "Vijay",
            13.40,
            80.50,
            Vehicle(
                "TN40GH2222",
                "Toyota",
                "Etios",
                "Blue",
                "Car"
            ),
            4.5
        )

        driver5 = Driver(
            105,
            "Ajay",
            13.15,
            80.30,
            Vehicle(
                "TN50JK9999",
                "Kia",
                "Sonet",
                "Grey",
                "Car"
            ),
            4.6
        )

        return [
            driver1,
            driver2,
            driver3,
            driver4,
            driver5
        ]