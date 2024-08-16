class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # not special index
        indice = []
        for i, (a, b) in enumerate(pairwise(nums)):
            if (a + b) % 2 == 0:
                indice.append(i)

        ans = []
        for _from, _to in queries:
            i = bisect_left(indice, _from)
            if i < len(indice) and indice[i] < _to:
                ans.append(False)
            else:
                ans.append(True)
        return ans 


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        s = list(accumulate((x % 2 == y % 2 for x, y in pairwise(nums)), initial=0))
        return [s[from_] == s[to] for from_, to in queries]


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        s = list(accumulate(((x ^ y ^ 1) & 1 for x, y in pairwise(nums)), initial=0))
        return [s[from_] == s[to] for from_, to in queries]


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        last_same = [0] * n
        for i in range(1, n):
            last_same[i] = i if nums[i - 1] % 2 == nums[i] % 2 else last_same[i - 1]
        return [last_same[to] <= from_ for from_, to in queries]
        
