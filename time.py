import datetime

time_mesurements = {
    "d" : ("d", "days", "dias", "dia"),
    "h" : ("h", "hours", "horas", "hora"),
    "m" : ("m", "minutes", "minutos", "minuto"),
    "s" : ("s", "seconds", "segundos", "segundos")
}

class Time:
    __seconds: int
    __minutes: int
    __hours: int
    __days: int
    time : str

    def __init__(self, time : str):
        self.time = time.replace(" ", "")


    def format_time(self):

