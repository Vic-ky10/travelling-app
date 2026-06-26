class Trackingservice:
    def move_driver(self , driver , new_latitude , new_longitude):
        driver.update_location(
            new_latitude,
            new_longitude
        )
        
        