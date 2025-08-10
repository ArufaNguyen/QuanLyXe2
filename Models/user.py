class User:
    def __init__(
        self, 
        username: str,
        password: str,
        role: str,
        qr_code: str,
        ID_xe: str = None,
        Time_used: int = 0,
        Time_started: str = None,
        Day_started: str = None,
        Day_Pass: int = 0,
        Slot_used: int = 0,
        On_slot: int = 0,
        plate_image_url: str = None
    ):
        self.username = username
        self.password = password
        self.role = role
        self.qr_code = qr_code
        self.ID_xe = ID_xe
        self.Time_used = Time_used
        self.Time_started = Time_started
        self.Day_started = Day_started
        self.Day_Pass = Day_Pass
        self.Slot_used = Slot_used
        self.On_slot = On_slot
        self.plate_image_url = plate_image_url

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "qr_code": self.qr_code,
            "ID_xe": self.ID_xe,
            "Time_used": self.Time_used,
            "Time_started": self.Time_started,
            "Day_started": self.Day_started,
            "Day_Pass": self.Day_Pass,
            "Slot_used": self.Slot_used,
            "On_slot": self.On_slot,
            "plate_image_url": self.plate_image_url
        }
