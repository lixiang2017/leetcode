class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        ans = []
        for p, n in zip(pos, neg):
            ans += [p, n]
        return ans
    
    
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p, n, ans = [], [], []
        for x in nums:
            if x > 0:
                p.append(x)
            else:
                n.append(x)
        for x, y in zip(p, n):
            ans.append(x)
            ans.append(y)
        return ans


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        i, j = 0, 1
        for x in nums:
            if x > 0:
                ans[i] = x
                i += 2
            else:
                ans[j] = x
                j += 2
        return ans

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        i = [0, 1]
        for x in nums:
            ans[i[x >> 63]] = x
            i[x >> 63] += 2
        return ans


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        i = [0, 1]
        for x in nums:
            ans[i[x >> 31]] = x
            i[x >> 31] += 2
        return ans
        