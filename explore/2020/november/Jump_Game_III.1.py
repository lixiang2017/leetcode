'''
BFS

You are here!
Your runtime beats 69.44 % of python submissions

Time: O(n)
Space: O(1)
memorize element which have been seen in original arr
'''


class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        deq = deque([start])
        
        while deq:
            cur = deq.popleft()
            if arr[cur] == 0:
                return True
            
            if arr[cur] < 0:  # have seen
                continue
            
            for i in [cur - arr[cur], cur + arr[cur]]:
                if 0 <= i < len(arr):
                    deq.append(i)
            
            arr[cur] = -1  # have seen, marked
        
        return False
