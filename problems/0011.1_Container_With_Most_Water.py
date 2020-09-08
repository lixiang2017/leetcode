'''
Success
Runtime: 108 ms, faster than 46.35% of Python online submissions for Container With Most Water.
Memory Usage: 13 MB, less than 74.58% of Python online submissions for Container With Most Water.
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        max_area = 0
        i = 0
        j = l - 1
        while i < j:
            tmp_area = (j - i) * min(height[i], height[j])
            max_area = max(tmp_area, max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print (Solution().maxArea(height))
    assert (Solution().maxArea(height) == 49)