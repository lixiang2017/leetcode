'''
BFS

Runtime: 108 ms, faster than 6.12% of Python3 online submissions for Numbers With Same Consecutive Differences.
Memory Usage: 14.1 MB, less than 73.81% of Python3 online submissions for Numbers With Same Consecutive Differences.
'''
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        # head
        for head in range(10):
            if head == 0 and n > 1:
                continue
            
            candidates = [[head]]
            for _ in range(n - 1):
                next_round = []
                for cand in candidates:
                    for c in set([cand[-1] - k, cand[-1] + k]):
                        if 0 <= c <= 9:
                            next_round.append(cand + [c])
                candidates = next_round
        
            ans.extend([int(''.join(str(c) for c in cand)) for cand in candidates])
            
        return ans 


'''
remove set([]), use choices

Runtime: 76 ms, faster than 31.63% of Python3 online submissions for Numbers With Same Consecutive Differences.
Memory Usage: 14.2 MB, less than 41.16% of Python3 online submissions for Numbers With Same Consecutive Differences.
'''
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        # head
        for head in range(10):
            if head == 0 and n > 1:
                continue

            candidates = [[head]]
            for _ in range(n - 1):
                next_round = []
                for cand in candidates:
                    choices = [cand[-1] - k, cand[-1] + k] if k != 0 else [cand[-1]]
                    for c in choices:
                        if 0 <= c <= 9:
                            next_round.append(cand + [c])
                candidates = next_round
        
            ans.extend([int(''.join(str(c) for c in cand)) for cand in candidates])
            
        return ans 



'''
do not transform to string, use integer directly

Runtime: 63 ms, faster than 57.82% of Python3 online submissions for Numbers With Same Consecutive Differences.
Memory Usage: 14.2 MB, less than 41.16% of Python3 online submissions for Numbers With Same Consecutive Differences.
'''
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        # head
        for head in range(10):
            if head == 0 and n > 1:
                continue
            
            candidates = [head]
            for _ in range(n - 1):
                next_round = []
                for cand in candidates:
                    tail = cand % 10
                    choices = [tail - k, tail + k] if k != 0 else [tail]
                    for c in choices:
                        if 0 <= c <= 9:
                            next_round.append(cand * 10 + c)
                candidates = next_round
            ans.extend(candidates)
            
        return ans 


