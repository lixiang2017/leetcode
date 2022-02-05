'''
hash table + sort + two pointers
T: O(2 * N^2 + 2 * N^2 * logN + 2 * N^2)

Runtime: 2168 ms, faster than 5.04% of Python3 online submissions for 4Sum II.
Memory Usage: 14.6 MB, less than 20.85% of Python3 online submissions for 4Sum II.
'''
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        ans = 0
        sum12, sum34 = Counter(), Counter()
        
        for i in range(n):
            for j in range(n):
                s = nums1[i] + nums2[j]
                sum12[s] += 1      
        for k in range(n):
            for l in range(n):
                s = nums3[k] + nums4[l]
                sum34[s] += 1
        # sorted
        ssum12 = sorted([(s, cnt) for s, cnt in sum12.items()])
        ssum34 = sorted([(s, cnt) for s, cnt in sum34.items()])
        n12, n34 = len(ssum12), len(ssum34)
        i, j = 0, n34 - 1
        while i < n12 and j >= 0:
            s12, cnt12 = ssum12[i]
            s34, cnt34 = ssum34[j]
            t = s12 + s34
            if t == 0:
                ans += cnt12 * cnt34
                i += 1
                j -= 1
            elif t > 0:
                j -= 1
            else:
                i += 1
        
        return ans
        
'''
hash table
T: O(4 * N + 2 * N^2)

Runtime: 524 ms, faster than 99.79% of Python3 online submissions for 4Sum II.
Memory Usage: 14.1 MB, less than 98.30% of Python3 online submissions for 4Sum II.
'''
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        c1, c2, c3, c4 = C(nums1), C(nums2), C(nums3), C(nums4)
        c12 = C()
        for x1, cnt1 in c1.items():
            for x2, cnt2 in c2.items():
                c12[x1 + x2] += cnt1 * cnt2
        
        ans = 0
        for x3, cnt3 in c3.items():
            for x4, cnt4 in c4.items():
                ans += c12[-x3 - x4] * cnt3 * cnt4
        
        return ans 
        

