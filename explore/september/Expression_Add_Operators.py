'''
BFS

You are here!
Your runtime beats 6.18 % of python3 submissions.
'''
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans, q, N, ops = [], deque([(0, '')]), len(num), '+-*'
        while q:
            idx, exp = q.popleft()
            if idx >= N:
                if eval(exp) == target:
                    ans.append(exp)
                continue
            if num[idx] == '0':
                if idx == N - 1:
                    q.append((N, exp + '0'))
                else:
                    for op in ops:
                        q.append((idx + 1, exp + '0' + op))
            else:
                for i in range(idx + 1, N):
                    for op in ops:
                        q.append((i, exp + num[idx: i] + op))
                    
                q.append((N, exp + num[idx:]))
        
        return ans
