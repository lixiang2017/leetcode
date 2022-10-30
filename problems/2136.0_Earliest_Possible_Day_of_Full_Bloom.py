'''
执行用时：268 ms, 在所有 Python3 提交中击败了85.37% 的用户
内存消耗：31.7 MB, 在所有 Python3 提交中击败了70.73% 的用户
通过测试用例：185 / 185

贪心 + 排序，优先让生长时间长的先种。
由于播种时间之和一定是最终答案固定的一部分，因此需要对生长时间进行贪心，长的越久的越先种，取其中最晚开花时间即为本题答案。
'''

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        pre = ans = 0
        for x, y in sorted(zip(plantTime, growTime), key = lambda x: x[1], reverse=True):
            pre += x 
            ans = max(ans, pre + y)
        return ans 
