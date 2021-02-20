'''
approach: Hash Table
Time: O(N + N) = O(N)
Space: O(N)

执行结果：
通过
显示详情
执行用时：56 ms, 在所有 Python 提交中击败了66.94%的用户
内存消耗：15.1 MB, 在所有 Python 提交中击败了33.06%的用户
'''


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        visited = defaultdict(list)
        mostTimes = 0
        for i, num in enumerate(nums):
            visited[num].append(i)
            if len(visited[num]) > mostTimes:
                mostTimes = len(visited[num])
        
        shortest = len(nums)
        for num, meet in visited.iteritems():
            if len(meet) == mostTimes:
                shortest = min(shortest, meet[-1] - meet[0] + 1)

        return shortest



'''
approach: Hash Table
Time: O(N + N) = O(N)
Space: O(N)

ref:
https://leetcode-cn.com/problems/degree-of-an-array/solution/shu-zu-de-du-by-leetcode-solution-ig97/

执行结果：
通过
显示详情
执行用时：68 ms, 在所有 Python 提交中击败了45.97%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了58.06%的用户
'''

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = {}
        mostTimes = 0
        for i, num in enumerate(nums):
            if num not in visited:
                visited[num] = [1, i, i]  # [count, start_idx, end_idx]
            else:
                visited[num][0] += 1
                visited[num][2] = i
            mostTimes = max(mostTimes, visited[num][0])

        shortest = len(nums)    
        for count, start_idx, end_idx in visited.itervalues():
            if count == mostTimes:
                span = end_idx - start_idx + 1
                shortest = min(shortest, span)

        return shortest



'''
approach: Hash Table
Time: O(N + N) = O(N)
Space: O(N)

ref:
https://leetcode-cn.com/problems/degree-of-an-array/solution/shu-zu-de-du-by-leetcode-solution-ig97/

执行结果：
通过
显示详情
执行用时：52 ms, 在所有 Python 提交中击败了79.84%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了53.22%的用户
'''

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = {}
        mostTimes = 0
        for i, num in enumerate(nums):
            if num not in visited:
                visited[num] = [1, i, i]  # [count, start_idx, end_idx]
            else:
                visited[num][0] += 1
                visited[num][2] = i
            # mostTimes = max(mostTimes, visited[num][0])

        shortest = len(nums)    
        for count, start_idx, end_idx in visited.itervalues():
            if mostTimes < count:
                mostTimes = count
                shortest = end_idx - start_idx + 1
            elif count == mostTimes:
                span = end_idx - start_idx + 1
                shortest = min(shortest, span)

        return shortest


