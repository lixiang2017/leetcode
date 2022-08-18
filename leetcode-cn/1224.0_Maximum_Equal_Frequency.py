'''
bucket sort

执行用时：312 ms, 在所有 Python3 提交中击败了29.17% 的用户
内存消耗：20.7 MB, 在所有 Python3 提交中击败了6.94% 的用户
通过测试用例：45 / 45
'''
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_cnt = max(c.values())
        bucket = [[] for _ in range(max_cnt)]
        max_bucket_id = -1
        ans = 1
        c1 = Counter()
        for i, x in enumerate(nums):
            bucket[c1[x]].append(x)
            if c1[x] > max_bucket_id:
                max_bucket_id = c1[x]
            # 1 or same + 1
            if (len(bucket[max_bucket_id]) == 1 and len(bucket[0]) * max_bucket_id == i) or \
                (len(bucket[0]) == len(bucket[max_bucket_id]) + 1 and len(bucket[max_bucket_id]) * (max_bucket_id + 1) == i) or 0 == max_bucket_id:
                ans = i + 1
            c1[x] += 1
        return ans 

