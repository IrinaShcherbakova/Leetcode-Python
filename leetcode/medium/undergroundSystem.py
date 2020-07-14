class Route:
    
    def __init__(self, name: str, time: int):
        self.name = name
        self.totalTime = time
        self.count = 1
        
    def addTime(self, time: int) -> None:
        self.totalTime += time
        self.count += 1
        
    def getAvTime(self) -> int:
        return self.totalTime / self.count


class UndergroundSystem:

    def __init__(self):
        self.routes = {}
        self.startStation = {}
        self.startTime = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.startStation[id] = stationName
        self.startTime[id] = t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.startStation[id]
        time = self.startTime[id]
        self.startStation.pop(id)
        self.startTime.pop(id)
        routeName = start + '#' + stationName
        routeTime = t - time
        if routeName in self.routes:
            self.routes[routeName].addTime(routeTime)
        else:
            self.routes[routeName] = Route(routeName, routeTime)
        
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = self.routes[startStation + '#' + endStation]
        return route.getAvTime()
        
        
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
