class Vehicle:
    def __init__(self, ID_xe: str, plate_image_url: str, time_started: str = None, day_started: str = None):
        self.ID_xe = ID_xe
        self.plate_image_url = plate_image_url
        self.time_started = time_started
        self.day_started = day_started
