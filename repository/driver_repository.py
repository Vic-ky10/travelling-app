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

        driver6 = Driver(
            106,
            "Meena",
            13.02,
            80.22,
            Vehicle(
                "TN60LM4321",
                "Tata",
                "Nexon",
                "Silver",
                "SUV"
            ),
            4.8
        )

        driver7 = Driver(
            107,
            "Sanjay",
            13.30,
            80.44,
            Vehicle(
                "TN70NP2468",
                "Mahindra",
                "XUV300",
                "White",
                "SUV"
            ),
            4.7
        )

        driver8 = Driver(
            108,
            "Divya",
            13.07,
            80.28,
            Vehicle(
                "TN80QR1357",
                "Skoda",
                "Slavia",
                "Blue",
                "Premium"
            ),
            4.9
        )

        return [
            driver1,
            driver2,
            driver3,
            driver4,
            driver5,
            driver6,
            driver7,
            driver8
        ]
