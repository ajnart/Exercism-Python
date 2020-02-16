class Clock:
    def __init__(self, hours, minutes):
        self.hour = (hours + (minutes // 60)) % 24
        self.minute = minutes % 60

    def __repr__(self):
        return 'Clock({0}, {1})'.format(self.hour, self.minute)
    
    def __str__(self):
        return("{0:02d}:{1:02d}".format(self.hour, self.minute))

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes) # TODO : Review this again.

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
