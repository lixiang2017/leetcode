'''
Prefix XOR
T: O(N^2)
S: O(N)

执行用时：60 ms, 在所有 Python3 提交中击败了62.74% 的用户
内存消耗：14.4 MB, 在所有 Python3 提交中击败了100.00% 的用户
'''


from operator import xor

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        
        triplets = 0
        pre_xor = [0] + list(accumulate(arr, xor))
        for i in range(1, N + 1):
            for j in range(i):
                if pre_xor[j] ^ pre_xor[i] == 0:
                    triplets += i - j - 1
        return triplets


'''
Prefix XOR + Hash Table
T: O(N + N) = O(N)
S: O(N + N) = O(N)

执行用时：44 ms, 在所有 Python3 提交中击败了83.01% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了97.39% 的用户
'''

from operator import xor

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        triplets = 0
        pre_xor = [0] + list(accumulate(arr, xor))
        cnt, total = Counter(), Counter()
        for i in range(N):
            if pre_xor[i + 1] in cnt:
                triplets += cnt[pre_xor[i + 1]] * i- total[pre_xor[i + 1]]
            cnt[pre_xor[i]] += 1
            total[pre_xor[i]] += i

        return triplets


'''
Prefix XOR + Hash Table
T: O(N)
S: O(N + N) = O(N)

执行用时：44 ms, 在所有 Python3 提交中击败了83.01% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了14.38% 的用户
'''

from operator import xor

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        triplets = 0
        pre = 0
        cnt, total = Counter(), Counter()
        for i, num in enumerate(arr):
            if (post := pre ^ num) in cnt:
                triplets += cnt[post] * i - total[post]
            cnt[pre] += 1
            total[pre] += i
            pre = post

        return triplets


