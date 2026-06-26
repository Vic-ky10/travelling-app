class User :
    def __init__(self, user_id , name , latitude , longitude):
        self.user_id = user_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        
    def update_location(self, latitude , longitude):    
        self.latitude = latitude
        self.longitude = longitude
        
    def display_info(self):
        print(f"user ID : {self.user_id}")
        print(f"Name : {self.name}")
        print(f"Location : {self.latitude}, {self.longitude}")    
    