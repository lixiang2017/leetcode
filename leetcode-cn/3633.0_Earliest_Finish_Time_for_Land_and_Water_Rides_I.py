class Solution:
    def solve(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_finish = min(s + d for s, d in zip(landStartTime, landDuration))
        return min(max(min_finish, s) + d for s, d in zip(waterStartTime, waterDuration))

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land_water = self.solve(landStartTime, landDuration, waterStartTime, waterDuration)
        water_land = self.solve(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(land_water, water_land)

class Solution:
    def solve(self, ans: int, s1: int, d1: int, s2: int, d2: int) -> int:
        return min(ans, max(s2 + d2, s1) + d1, max(s1 + d1, s2) + d2)

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = inf
        for s1, d1 in zip(landStartTime, landDuration):
            for s2, d2 in zip(waterStartTime, waterDuration):
                ans = self.solve(ans, s1, d1, s2, d2)
        return ans