'''
Runtime: 287 ms, faster than 60.99% of Python3 online submissions for Design Underground System.
Memory Usage: 25.3 MB, less than 31.03% of Python3 online submissions for Design Underground System.
'''
class UndergroundSystem:

    def __init__(self):
        # (start, end) -> total length
        self.travel_len = defaultdict(int)
        # (start, end) -> count
        self.travel_cnt = defaultdict(int)
        # person_id -> [startStation, enterTime]
        self.id2enter = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id2enter[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, enterTime = self.id2enter[id]
        self.id2enter[id] = []
        self.travel_len[(startStation, stationName)] += t - enterTime
        self.travel_cnt[(startStation, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return 1.0 * self.travel_len[(startStation, endStation)] / self.travel_cnt[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
