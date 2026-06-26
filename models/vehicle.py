class Vehicle:

    def __init__(self, vehicle_number, brand, model, color, vehicle_type):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.model = model
        self.color = color
        self.vehicle_type = vehicle_type

    def display_info(self):
        print(f"Vehicle Number : {self.vehicle_number}")
        print(f"Brand          : {self.brand}")
        print(f"Model          : {self.model}")
        print(f"Color          : {self.color}")
        print(f"Type           : {self.vehicle_type}")