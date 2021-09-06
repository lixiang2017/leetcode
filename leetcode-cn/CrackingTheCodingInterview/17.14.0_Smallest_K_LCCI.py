'''
执行用时：60 ms, 在所有 Python3 提交中击败了84.40% 的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了82.67% 的用户
通过测试用例：29 / 29
'''
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]


'''
执行用时：100 ms, 在所有 Python3 提交中击败了39.31% 的用户
内存消耗：23.1 MB, 在所有 Python3 提交中击败了5.07% 的用户
通过测试用例：29 / 29
'''
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        return nsmallest(k, arr)


'''
执行用时：68 ms, 在所有 Python3 提交中击败了74.27% 的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了86.32% 的用户
通过测试用例：29 / 29
'''
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        heapify(arr)
        ans = []
        while k:
            ans.append(heappop(arr))
            k -= 1
        return ans

