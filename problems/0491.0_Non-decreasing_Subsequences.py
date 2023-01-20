'''
Runtime: 266 ms, faster than 52.97% of Python3 online submissions for Non-decreasing Subsequences.
Memory Usage: 27.1 MB, less than 5.00% of Python3 online submissions for Non-decreasing Subsequences.
'''
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        def backtrack(cur: List[int], i: int) -> None:
            if len(cur) >= 2:
                ans.append(cur)
            if i == n:
                return
            # choose
            if not cur or cur[-1] <= nums[i]:
                backtrack(cur + [nums[i]], i + 1)
            # not choose
            backtrack(cur, i + 1)
        
        backtrack([], 0)
        ans = set(tuple(arr) for arr in ans)
        return [list(arr) for arr in ans]
        

'''
去重

Runtime: 212 ms, faster than 97.03% of Python3 online submissions for Non-decreasing Subsequences.
Memory Usage: 21.6 MB, less than 85.78% of Python3 online submissions for Non-decreasing Subsequences.
'''
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        def backtrack(cur: List[int], i: int) -> None:
            if i == n:
                if len(cur) >= 2:
                    ans.append(cur)
                return
            # choose
            if not cur or cur[-1] <= nums[i]:
                backtrack(cur + [nums[i]], i + 1)
            # not choose
            if not cur or cur[-1] != nums[i]:
                backtrack(cur, i + 1)
        
        backtrack([], 0)
        return ans 
        

'''
real backtrack

Runtime: 219 ms, faster than 91.09% of Python3 online submissions for Non-decreasing Subsequences.
Memory Usage: 21.7 MB, less than 62.66% of Python3 online submissions for Non-decreasing Subsequences.
'''
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        def backtrack(cur: List[int], i: int) -> None:
            if i == n:
                if len(cur) >= 2:
                    ans.append(cur[:])
                return
            # choose
            if not cur or cur[-1] <= nums[i]:
                cur.append(nums[i])
                backtrack(cur, i + 1)
                cur.pop()
            # not choose
            if not cur or cur[-1] != nums[i]:
                backtrack(cur, i + 1)
        
        backtrack([], 0)
        return ans 


'''
二进制枚举 + Rabin-Karp Hash

Runtime: 1087 ms, faster than 9.07% of Python3 online submissions for Non-decreasing Subsequences.
Memory Usage: 23.2 MB, less than 20.78% of Python3 online submissions for Non-decreasing Subsequences.
'''
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        seen_hash = set()
        BASE, MOD = 211, 10 ** 9 + 7
        
        def sequence(mask):
            seq = []
            for i in range(n):
                if mask & 1:
                    seq.append(nums[i])
                mask >>= 1
            return seq 
        
        def check(seq):
            if len(seq) < 2:
                return False
            for a, b in pairwise(seq):
                if a > b:
                    return False
            return True
        
        def get_hash(seq, base, mod):
            hash_value = 0
            for x in seq:
                hash_value = hash_value * base % mod + (x + 101)
                hash_value %= mod
            return hash_value
        
        for mask in range(1 << n):
            seq = sequence(mask)
            if check(seq):
                hash_value = get_hash(seq, BASE, MOD)
                if hash_value not in seen_hash:
                    ans.append(seq)
                    seen_hash.add(hash_value)
        return ans 
        
