'''
approach: Prefix XOR (Prefix Sum)
Time: O(N + k), where N is the length of arr, k is the length of queries.
Space: O(N)

执行用时：400 ms, 在所有 Python3 提交中击败了91.03% 的用户
内存消耗：29.5 MB, 在所有 Python3 提交中击败了5.13% 的用户
'''


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        N = len(arr)
        pre_xor = [0] * (N + 1)
        for i in range(N):
            pre_xor[i + 1] = pre_xor[i] ^ arr[i]
            
        return [pre_xor[l] ^ pre_xor[r + 1] for l, r in queries]
