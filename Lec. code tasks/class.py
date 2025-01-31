class Time():
    def __init__(self, sec, min, hour):
        self.time = sec+60*min+3600*hour
        self.sec = sec%60
        self.min = min%60
        self.hour = hour%24

    def __str__(self):
        return f"{self.hour}:{self.min}:{self.sec}"

    def __updateTimeFormat(self):
        self.sec= self.time%60
        self.min= self.time//60%60
        self.hour = self.time//3600%24

    def increment_sec(self, plus=1):
        self.time+=plus
        self.sec= self.time%60
    def decrement_sec(self, minus=1):
        self.time-=minus
        self.sec= self.time%60

    def increment_min(self, plus=1):
        self.time+=plus*60
        self.min= self.time//60%60
    def decrement_min(self, minus=1):
        self.time-=self.time//60%60
        self.min= self.time//60%60

    def increment_hour(self, plus=1):
        self.time+=plus*3600
        self.hour = self.time//3600%24
    def decrement_hour(self, minus=1):
        self.hour-=minus*3600
        self.hour = self.time//3600%24

    #or another way by using other magic methods(add and sub) we can just write:

    def __add__(self, sec):
        self.time+=sec
        self.__updateTimeFormat()
        return self.__str__()
    
    def __sub__(self, sec):
        self.time-=sec
        self.__updateTimeFormat()
        return self.__str__()

x = Time(1,2,3)
y = Time(100, 101, 102)
print(x)
print(x+3661)
print(y)