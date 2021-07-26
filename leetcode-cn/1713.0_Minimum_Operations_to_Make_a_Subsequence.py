'''
Hash Table + Greedy + Binary Search(DP),T:O(NlogN),S:O(N)
LCS(longest common subsequence)-> LIS(longest increasing subsequence)

执行用时：192 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：36.8 MB, 在所有 Python3 提交中击败了96.30% 的用户
'''
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        pos = {num: idx for idx, num in enumerate(target)}
        len2idx = []
        for num in arr:
            if num in pos:
                idx = pos[num]
                if not len2idx or len2idx[-1] < idx:
                    len2idx.append(idx)
                else:
                    len2idx[bisect.bisect_left(len2idx, idx)] = idx
        return len(target) - len(len2idx)
