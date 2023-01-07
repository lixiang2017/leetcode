'''
Greedy
T: O(N)
S: O(1)

ref:
https://leetcode.com/problems/gas-station/discuss/42568/Share-some-of-my-ideas.

I have thought for a long time and got two ideas:

    If car starts at A and can not reach B. Any station between A and B
    can not reach B.(B is the first station that A can not reach.)
    If the total number of gas is bigger than the total number of cost. There must be a solution.
    (Should I prove them?)


Runtime: 739 ms, faster than 22.25% of Python3 online submissions for Gas Station.
Memory Usage: 18.8 MB, less than 75.25% of Python3 online submissions for Gas Station.
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = tank = 0
        for i, g in enumerate(gas):
            tank += g - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0

        return start

'''
https://leetcode.cn/problems/gas-station/comments/

补充两个问题（2019/5/26）：
问题1: 为什么应该将起始站点设为k+1？
    因为k->k+1站耗油太大，0->k站剩余油量都是不为负的，每减少一站，就少了一些剩余油量。所以如果从k前面的站点作为起始站，剩余油量不可能冲过k+1站。
问题2: 为什么如果k+1->end全部可以正常通行，且rest>=0就可以说明车子从k+1站点出发可以开完全程？
    因为，起始点将当前路径分为A、B两部分。其中，必然有(1)A部分剩余油量<0。(2)B部分剩余油量>0。
    所以，无论多少个站，都可以抽象为两个站点（A、B）。(1)从B站加满油出发，(2)开往A站，车加油，(3)再开回B站的过程。
重点：B剩余的油>=A缺少的总油。必然可以推出，B剩余的油>=A站点的每个子站点缺少的油。

Runtime: 674 ms, faster than 93.43% of Python3 online submissions for Gas Station.
Memory Usage: 18.9 MB, less than 90.27% of Python3 online submissions for Gas Station.
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        run = rest = ans = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            run += g - c
            rest += g - c
            if run < 0:
                run = 0
                ans = i + 1
        return -1 if rest < 0 else ans
