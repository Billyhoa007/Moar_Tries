class show:
    def __init__(self, name, beginTime, endTime, dayofweek, counter):
        self.name = name
        self.begintTime = beginTime
        self.endTime = endTime
        self.dayofweek = dayofweek
        self.counter = counter


class record:
    def __init__(self, ip, logTime, dayofweek):
        self.ip = ip
        self.logTime = logTime
        self.dayofweek = dayofweek


# I have no idea what I am doing...