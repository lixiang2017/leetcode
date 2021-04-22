'''
Hash Table

[[1],[1],[1]]


4 / 85 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
Last executed input:
[[100000000],[100000000],[100000000]]
'''

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # up = [0] * sum(wall[0])
        up = [0 for _ in range(sum(wall[0]))]
        Height = len(wall)
        '''
        for row in wall:
            idx = -1
            for brick in row:
                idx += brick
                up[idx] += 1
        '''
        max_up = 0
        for bricks in wall:
            N = len(bricks)
            idx = -1
            for i in range(N):
                idx += bricks[i]
                up[idx] += 1
                if i != N - 1 and up[idx] > max_up:
                    max_up = up[idx]
        return Height - max_up
        # print(up)
        # return len(wall) - max(up[: -1]) if up[: -1] else len(wall)


'''
approach: Hash Table
Time: O(N), where N the number of bricks in the wall.
Space: O(N), for hash table.

You are here!
Your runtime beats 56.82 % of python3 submissions.
You are here!
Your memory usage beats 86.13 % of python3 submissions.
'''

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        Height = len(wall)
        seen_ups = defaultdict(int)
        max_up = 0
        for bricks in wall:
            N = len(bricks)
            idx = 0
            for i in range(N - 1):
                idx += bricks[i]
                seen_ups[idx] += 1
                if seen_ups[idx] > max_up:
                    max_up = seen_ups[idx]
            
        return Height - max_up


'''
You are here!
Your runtime beats 84.56 % of python3 submissions.
You are here!
Your memory usage beats 62.64 % of python3 submissions.
'''

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        up = defaultdict(int)
        for row in wall:
            cur_sum = 0
            for brick in row[: -1]:
                cur_sum += brick
                up[cur_sum] += 1
        
        return len(wall) - max(up.values(), default=0)
        

'''
You are here!
Your runtime beats 56.82 % of python3 submissions.
You are here!
Your memory usage beats 86.13 % of python3 submissions.
'''

from collections import defaultdict
from itertools import accumulate

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        broken = defaultdict(int)
        
        for row in wall:
            for x in accumulate(row[: -1]):
                broken[x] -= 1
                
        return len(wall) + min(broken.values(), default=0)