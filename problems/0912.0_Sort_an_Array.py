'''
quick sort

Runtime: 780 ms, faster than 54.59% of Python3 online submissions for Sort an Array.
Memory Usage: 22.8 MB, less than 21.48% of Python3 online submissions for Sort an Array.
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        p = random.choice(nums)
        small = [x for x in nums if x < p]
        eq = [x for x in nums if x == p]
        greater = [x for x in nums if x > p]
        return self.sortArray(small) + eq + self.sortArray(greater)


'''
merge sort

Runtime: 724 ms, faster than 65.36% of Python3 online submissions for Sort an Array.
Memory Usage: 22.1 MB, less than 36.69% of Python3 online submissions for Sort an Array.
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        
        def merge(a, b):
            na, nb = len(a), len(b)
            ans = []
            i = j = 0
            while i < na and j < nb:
                if a[i] < b[j]:
                    ans.append(a[i])
                    i += 1
                else:
                    ans.append(b[j])
                    j += 1
            ans.extend(a[i:])
            ans.extend(b[j:])
            return ans
        
        mid = len(nums) // 2
        a = self.sortArray(nums[: mid])
        b = self.sortArray(nums[mid: ])
        return merge(a, b)
