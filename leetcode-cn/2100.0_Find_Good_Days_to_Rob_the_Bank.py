'''
T: O(2N)
S: O(2N)

执行用时：236 ms, 在所有 Python3 提交中击败了44.90% 的用户
内存消耗：46.5 MB, 在所有 Python3 提交中击败了5.09% 的用户
通过测试用例：144 / 144
'''
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        forward, backward = defaultdict(int), defaultdict(int)
        n = len(security)
        for i in range(n - 2, time - 1, -1):
            if security[i] <= security[i + 1]:
                backward[i] = backward[i + 1] + 1
        
        ans = []
        for i in range(n - time):
            if i >= 1 and security[i] <= security[i - 1]:
                forward[i] = forward[i - 1] + 1
            # 输入：security = [1,1,1,1,1], time = 0
            # 输出：[0,1,2,3,4]
            if forward[i] >= time and backward[i] >= time:
                ans.append(i)

        return ans

'''
T: O(2N)
S: O(2N)

执行用时：176 ms, 在所有 Python3 提交中击败了83.14% 的用户
内存消耗：31.2 MB, 在所有 Python3 提交中击败了64.31% 的用户
通过测试用例：144 / 144
'''
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        forward, backward = [0] * n, [0] * n
        for i in range(n - 2, time - 1, -1):
            if security[i] <= security[i + 1]:
                backward[i] = backward[i + 1] + 1
        
        ans = []
        for i in range(n - time):
            if i >= 1 and security[i] <= security[i - 1]:
                forward[i] = forward[i - 1] + 1
            if forward[i] >= time and backward[i] >= time:
                ans.append(i)
        return ans

