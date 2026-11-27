class Clock:
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self._normalize()

    def _normalize(self):
        extra_hours, self.minute = divmod(self.minute, self.MINUTES_PER_HOUR)
        self.hour = (self.hour + extra_hours) % self.HOURS_PER_DAY
        
    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
