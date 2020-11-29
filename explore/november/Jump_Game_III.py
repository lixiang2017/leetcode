'''
BFS

You are here!
Your runtime beats 96.76 % of python submissions.

Time: O(n)
Space: O(n)
'''



class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        if 0 not in arr:
            return False
        
        size = len(arr)
        seen_index = set()
        deq = deque([start])
        while deq:
            one = deq.popleft()
            seen_index.add(one)
            if arr[one] == 0:
                return True
            plus = one + arr[one]
            if 0 <= plus <= size - 1 and plus not in seen_index:
                deq.append(plus)
            minus = one - arr[one]
            if 0 <= minus <= size - 1 and minus not in seen_index:
                deq.append(minus)
            
        return False


'''
Submission Result: Time Limit Exceeded 
Last executed input:
[3,0,2,1,2]
2
# need to use seen_index to memorise the seen indice
'''


