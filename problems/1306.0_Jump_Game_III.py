'''
BFS

Runtime: 377 ms, faster than 23.33% of Python3 online submissions for Jump Game III.
Memory Usage: 20.8 MB, less than 84.22% of Python3 online submissions for Jump Game III.
'''
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = deque([start])
        seen = set([start])
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            for ni in [i + arr[i], i - arr[i]]:
                if 0 <= ni < n and ni not in seen:
                    q.append(ni)
                    seen.add(ni)
        
        return False


'''
BFS

Runtime: 490 ms, faster than 8.83% of Python3 online submissions for Jump Game III.
Memory Usage: 20.8 MB, less than 84.22% of Python3 online submissions for Jump Game III.
'''
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = deque([start])
        seen = set()
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            seen.add(i)
            for ni in [i + arr[i], i - arr[i]]:
                if 0 <= ni < n and ni not in seen:
                    q.append(ni)
                   
        return False
