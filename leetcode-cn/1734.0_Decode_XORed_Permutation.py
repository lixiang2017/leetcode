'''
approach: XOR
Time: O(N + N) = O(N)
Space: O(N)

执行用时：156 ms, 在所有 Python3 提交中击败了97.56%的用户
内存消耗：30.6 MB, 在所有 Python3 提交中击败了13.42%的用户
'''


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        all_xor = 0
        N = len(encoded) + 1
        if N % 4 == 1:
            all_xor = 1
        elif N % 4 == 2:
            all_xor = 3
        
        all_but_0 = 0
        for i in range(1, N, 2):
            all_but_0 ^= encoded[i]
        
        perm0 = all_xor ^ all_but_0
        perm = [perm0]
        for en in encoded:
            perm.append(perm[-1] ^ en)

        return perm
