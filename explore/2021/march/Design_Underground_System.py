'''
approach: Two Hash Tables
You are here!
Your runtime beats 51.06 % of python submission
You are here!
Your memory usage beats 70.09 % of python submissions.

# checks
id -> (station, time)   # checkIn

   ^
   |
# to build
(StartStation, EndStation) -> [delta1, delta2, delta3, ...]
'''


class UndergroundSystem(object):

    def __init__(self):
        self.checks = {}
        self.trips = defaultdict(list)

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checks[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.trips[(self.checks[id][0], stationName)].append(t - self.checks[id][1])
        del self.checks[id] 
            

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        return sum(self.trips[(startStation, endStation)]) * 1.0 / len(self.trips[(startStation, endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
