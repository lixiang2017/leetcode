'''
hash table + sort + two pointers

Runtime: 163 ms, faster than 49.42% of Python3 online submissions for 3Sum With Multiplicity.
Memory Usage: 14 MB, less than 92.44% of Python3 online submissions for 3Sum With Multiplicity.
'''
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        freq = Counter(arr)
        nums = sorted(freq.keys())
        n = len(nums)
        ans = 0
        
        # k i j
        for k in range(n):    
            i, j = k, n - 1
            while i <= j:
                s = nums[k] + nums[i] + nums[j]
                if s > target:
                    j -= 1
                elif s < target:
                    i += 1
                else:
                    if k == i == j:
                        f = freq[nums[k]]
                        if f >= 3:
                            ans += f * (f - 1) * (f - 2)// 6
                    elif k == i:
                        f = freq[nums[k]]
                        if f >= 2:
                            ans += f * (f - 1) * freq[nums[j]] // 2
                    elif i == j:
                        f = freq[nums[i]]
                        if f >= 2:
                            ans += f * (f - 1) * freq[nums[k]] // 2
                    else:
                        ans += freq[nums[k]] * freq[nums[i]] * freq[nums[j]]
                    i += 1
                    j -= 1
                    ans %= MOD 
        
        return ans
