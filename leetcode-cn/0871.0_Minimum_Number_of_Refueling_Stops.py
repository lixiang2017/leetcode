'''
brute force
120 / 198 个通过测试用例
状态：超出时间限制
'''
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        if stations and startFuel < stations[0][0]:
            return -1
        total = sum(s[1] for s in stations)
        if startFuel + total < target:
            return -1
        # try refuel all
        start = startFuel 
        for i, (p, f) in enumerate(stations):
            start -= p 
            if i >= 1:
                start += stations[i - 1][0]
            if start < 0:
                return -1 
            start += f 
        
        n = len(stations)
        ans = n
        def dfs(currentFuel, idx, refuel_cnt):
            nonlocal ans 
            if refuel_cnt >= ans:
                return 
            if currentFuel < 0:
                return 
            if idx > n:
                # print('refuel_cnt: ', refuel_cnt, path)
                ans = min(ans, refuel_cnt)
                return 
            # add 
            prev_position = 0 if idx == 0 else stations[idx-1][0]
            cur_position = stations[idx][0] if idx < n else target
            if idx < n and currentFuel - (cur_position - prev_position) >= 0:
                dfs(currentFuel - (cur_position - prev_position) + stations[idx][1], idx + 1, refuel_cnt + 1)
            # not add 
            dfs(currentFuel - (cur_position - prev_position), idx + 1, refuel_cnt)

        dfs(startFuel, 0, 0)
        return ans 

'''
有可能中间某一步达不到

通过测试用例：54 / 198
输入：
1000
83
[[25,27],[36,187],[140,186],[378,6],[492,202],[517,89],[579,234],[673,86],[808,53],[954,49]]
输出：
6
预期结果：
-1

49 / 198 个通过测试用例
状态：解答错误
提交时间：几秒前
最后执行的输入：
100
25
[[25,25],[50,25],[75,25]]

必须能到了 idx=5, 才能加上idx=5的油
通过测试用例：55 / 198
输入：
1000
299
[[13,100],[25,117],[122,82],[189,123],[268,56],[382,214],[408,280],[421,272],[589,110],[899,4]]
输出：
3
预期结果：
4

refuel_cnt:  9 [0, 1, 2, 3, 4, 5, 6, 7, 8]
refuel_cnt:  8 [0, 1, 2, 3, 4, 5, 6, 7]
refuel_cnt:  7 [0, 1, 2, 3, 4, 5, 6]
refuel_cnt:  6 [0, 1, 2, 3, 4, 6]
refuel_cnt:  5 [0, 1, 2, 3, 6]
refuel_cnt:  4 [0, 1, 5, 6]

120 / 198 个通过测试用例
状态：超出时间限制
提交时间：几秒前
最后执行的输入：
1000
36
[[7,13],[10,11],[12,31],[22,14],[32,26],[38,16],[50,8],[54,13],[75,4],[85,2],[88,35],[90,9],[96,35],[103,16],[115,33],[121,6],[123,1],[138,2],[139,34],[145,30],[149,14],[160,21],[167,14],[188,7],[196,27],[248,4],[256,35],[262,16],[264,12],[283,23],[297,15],[307,25],[311,35],[316,6],[345,30],[348,2],[354,21],[360,10],[362,28],[363,29],[367,7],[370,13],[402,6],[410,32],[447,20],[453,13],[454,27],[468,1],[470,8],[471,11],[474,34],[486,13],[490,16],[495,10],[527,9],[533,14],[553,36],[554,23],[605,5],[630,17],[635,30],[640,31],[646,9],[647,12],[659,5],[664,34],[667,35],[676,6],[690,19],[709,10],[721,28],[734,2],[742,6],[772,22],[777,32],[778,36],[794,7],[812,24],[813,33],[815,14],[816,21],[824,17],[826,3],[838,14],[840,8],[853,29],[863,18],[867,1],[881,27],[886,27],[894,26],[917,3],[953,6],[956,3],[957,28],[962,33],[967,35],[972,34],[984,8],[987,12]]
'''


'''
pq + greedy

执行用时：48 ms, 在所有 Python3 提交中击败了55.63% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了90.78% 的用户
通过测试用例：198 / 198
'''
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        ans, fuel, h, prev = 0, startFuel, [], 0
        stations.append([target, 0])
        for p, f in stations:
            # distance
            d = p - prev 
            fuel -= d 
            while fuel < 0 and h:
                fuel -= heappop(h)
                ans += 1
            if fuel < 0:
                return -1
            prev = p
            heappush(h, -f)
        return ans 



