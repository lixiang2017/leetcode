'''
sort + two pointers
T: O(NlogN + N)
S: O(logN)

Runtime: 924 ms, faster than 37.50% of Python3 online submissions for Max Number of K-Sum Pairs.
Memory Usage: 26.3 MB, less than 91.29% of Python3 online submissions for Max Number of K-Sum Pairs.
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        l, r = 0, n - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                ans += 1
                l += 1
                r -= 1
            elif s > k:
                r -= 1
            else:
                l += 1
        
        return ans 



'''
sort + two pointers + pruning
T: O(NlogN + N)
S: O(logN)

Runtime: 1074 ms, faster than 20.76% of Python3 online submissions for Max Number of K-Sum Pairs.
Memory Usage: 26.3 MB, less than 91.29% of Python3 online submissions for Max Number of K-Sum Pairs.
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        l, r = 0, n - 1
        while l < r and nums[l] < k:    #  pruning:  nums[left] < k
            s = nums[l] + nums[r]
            if s == k:
                ans += 1
                l += 1
                r -= 1
            elif s > k:
                r -= 1
            else:
                l += 1
        
        return ans 


'''
hash table
T: O(N)
S: O(N)

Runtime: 1163 ms, faster than 12.06% of Python3 online submissions for Max Number of K-Sum Pairs.
Memory Usage: 27.6 MB, less than 5.13% of Python3 online submissions for Max Number of K-Sum Pairs.
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        ans = 0
        for x in nums:
            complement = k - x
            if freq[complement] > 0:
                ans += 1
                freq[complement] -= 1
            else:
                freq[x] += 1
        return ans 

'''
hash table
T: O(2N)
S: O(N)


Runtime: 809 ms, faster than 58.48% of Python3 online submissions for Max Number of K-Sum Pairs.
Memory Usage: 27 MB, less than 54.91% of Python3 online submissions for Max Number of K-Sum Pairs.
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        ans = 0
        for x, c in freq.items():
            if x * 2 == k:
                ans += c // 2
                freq[x] = 0
            elif k - x in freq:
                pair_cnt = min(freq[x], freq[k - x])
                ans += pair_cnt
                freq[x] = 0
                freq[k - x] = 0
        return ans 




