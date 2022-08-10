'''
DP + two pointers
T: O(N^2)
S: O(N)

Runtime: 2542 ms, faster than 11.61% of Python3 online submissions for Binary Trees With Factors.
Memory Usage: 13.9 MB, less than 99.49% of Python3 online submissions for Binary Trees With Factors.
'''
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # need to sort first
        arr.sort()
        n = len(arr)
        MOD = 10 ** 9 + 7
        cnt = [1] * n 
        # i..j
        for k in range(1, n):
            i, j = 0, k - 1
            while i < k and j >= 0:
                if arr[i] * arr[j] == arr[k]:
                    cnt[k] += cnt[i] * cnt[j]
                    cnt[k] %= MOD
                    i += 1
                    j -= 1
                elif arr[i] * arr[j] > arr[k]:
                    j -= 1
                else:
                    i += 1
        return sum(cnt) % MOD 
    
'''
Input
[18,31,2,4,14,7,9,63,10,84]
Output
27
Expected
17
 
Input
[45,42,2,18,23,1170,12,41,40,9,47,24,33,28,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43,15,4,16,35,25,20,44,5,48]
Output
612
Expected
777
'''



'''
DP + hash table
T: O(N^2)
S: O(N)

Runtime: 481 ms, faster than 79.29% of Python3 online submissions for Binary Trees With Factors.
Memory Usage: 14.2 MB, less than 30.81% of Python3 online submissions for Binary Trees With Factors.
'''
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        MOD = 10 ** 9 + 7
        cnt = [1] * n 
        index = {x: i for i, x in enumerate(arr)}
        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0:
                    another = x // arr[j]
                    if another in index:
                        cnt[i] += cnt[j] * cnt[index[another]]
                        cnt[i] %= MOD 
        return sum(cnt) % MOD 
    