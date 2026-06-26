class Ride:
    
    def __init__(self, ride_id , passenger, driver , pickup , drop):
        
        self.ride_id = ride_id
        self.passenger = passenger
        self.driver = driver
        self.pickup = pickup
        self.drop = drop 
        self.vehicle = driver.vehicle
        
        self.status = "Requested"
        
    def start_ride(self):
        self.status = "started"
    
    def complete_ride(self):
        self.status = "completed"
        
    def display_ride(self):

        print(f"Ride ID : {self.ride_id}")

        print(f"Passenger : {self.passenger.name}")

        print(f"Driver : {self.driver.name}")

        print(f"Vehicle : {self.vehicle.vehicle_number}")

        print(f"Pickup : {self.pickup}")

        print(f"Drop : {self.drop}")

        print(f"Status : {self.status}")