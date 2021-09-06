'''
Greedy + Heap

执行用时：124 ms, 在所有 Python3 提交中击败了60.40% 的用户
内存消耗：25.9 MB, 在所有 Python3 提交中击败了48.52% 的用户
通过测试用例：51 / 51

ref:
https://leetcode-cn.com/problems/p0NxJO/solution/java-tan-xin-by-feilue-mawl/

先求数组和

    如果为负数，怎么移动都到不了最后一个房间
    如果非负数，那么就肯定能到达最后一个房间

使用优先队列存储所有已经经过的怪物房间（会扣血的房间）

如果到达一个房间后血量 ≤0，就取出队列中最小的元素（扣血最多的房间）放到末尾并把血量加回来

    因为是到达这个房间以后血量才不够的，队列中最小的元素必定小于等于当前房间，也必定能将血量变正，所以只用取出一次
    因为数组和大于000所以在最后必定会有足够的血量来访问这个扣血的房间，所以取出之后就可以不用管了

每次执行完之后加上一次操作的次数即可
'''
class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0:
            return -1

        presum = 1
        h = []
        N = len(nums)
        ans = 0
        for i in range(N):
            presum += nums[i]
            if nums[i] < 0:
                heapq.heappush(h, nums[i])
            if presum <= 0:
                ans += 1
                minn = heapq.heappop(h)
                presum += -minn
        return ans 
