'''
k * k

执行用时：720 ms, 在所有 Python3 提交中击败了25.66% 的用户
内存消耗：118.1 MB, 在所有 Python3 提交中击败了16.39% 的用户
通过测试用例：32 / 32
'''
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # ks = nsmallest(k, [(x + y, x, y) for x in nums1 for y in nums2])
        ks = nsmallest(k, [(nums1[i] + nums2[j], nums1[i], nums2[j]) \
            for i in range(min(k, len(nums1))) for j in range(min(k, len(nums2)))])
        return [[x, y]for _sum, x, y in ks]


'''
Runtime: 2795 ms, faster than 5.04% of Python3 online submissions for Find K Pairs with Smallest Sums.
Memory Usage: 35.4 MB, less than 63.07% of Python3 online submissions for Find K Pairs with Smallest Sums.
'''
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        left, right = nums1[0] + nums2[0], nums1[-1] + nums2[-1]
        
        def check(mid):
            # count sum(x and y) <= mid
            cnt = 0
            for x in nums1:
                idx = bisect_right(nums2, mid - x)
                cnt += idx
            return cnt >= k
        
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        target_sum = right + 1
        ans = []
        for x in nums1:
            for y in nums2:
                if x + y <= target_sum:
                    ans.append([x, y])
                else:
                    break
        
        ans.sort(key=lambda pair: sum(pair))
        return ans[: k]

'''
Runtime: 2785 ms, faster than 5.04% of Python3 online submissions for Find K Pairs with Smallest Sums.
Memory Usage: 35.2 MB, less than 69.98% of Python3 online submissions for Find K Pairs with Smallest Sums.
'''
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        left, right = nums1[0] + nums2[0], nums1[-1] + nums2[-1]
        
        def check(mid):
            # count sum(x and y) <= mid
            cnt = 0
            for x in nums1:
                idx = bisect_right(nums2, mid - x)
                cnt += idx
            return cnt >= k
        
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        target_sum = right + 1
        ans = []
        equal = []
        for x in nums1:
            for y in nums2:
                if x + y < target_sum:
                    ans.append([x, y])
                elif x + y == target_sum:
                    equal.append([x, y])
                else:
                    break
        
        return ans + equal[: k - len(ans)]
