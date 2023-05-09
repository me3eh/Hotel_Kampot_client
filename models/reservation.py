class Reservation:
    def __init__(self, params):
        self.id = params["id"]
        self.room_number = params["room_number"]
        self.from_date = params["from"]
        self.to_date = params["to"]

    def __str__(self):
        return "Reservation with id: %s, room number: %s, from date: %s, to date: %s" %\
               (self.id, self.room_number, self.from_date, self.to_date)
