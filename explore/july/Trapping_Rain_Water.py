'''
approach: Two Pointers
Time: O(2N) = O(N)
Space: O(N)

You are here!
Your runtime beats 92.74 % of python3 submissions.
You are here!
Your memory usage beats 87.21 % of python3 submissions.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        if N < 3:
            return 0
        
        pre_max = [height[0]] * N
        post_max = height[-1]
        total = 0
        for i in range(1, N):
            pre_max[i] = max(pre_max[i - 1], height[i])
        for i in range(N - 1, -1, -1):
            post_max = max(post_max, height[i])
            total += min(post_max, pre_max[i]) - height[i]
        return total


'''
approach: Two Pointers
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 97.90 % of python3 submissions.
You are here!
Your memory usage beats 87.21 % of python3 submissions.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ans = left_max = right_max = 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans


'''
approach: Two Pointers
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 97.90 % of python3 submissions.
You are here!
Your memory usage beats 66.86 % of python3 submissions.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        ans = 0
        lmax, rmax = height[0], height[-1]
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] > lmax:
                lmax = height[l]
            if height[r] > rmax:
                rmax = height[r]
            # fill water
            if lmax < rmax:
                ans += lmax - height[l]
                l += 1
            else:
                ans += rmax - height[r]
                r -= 1
        return ans


