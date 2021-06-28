'''
approach: Greedy
Time: O(2N) = O(N)
Space: O(N)

You are here!
Your runtime beats 51.59 % of python3 submissions.
You are here!
Your memory usage beats 25.14 % of python3 submissions.

ref:
https://leetcode-cn.com/problems/candy/solution/fen-fa-tang-guo-by-leetcode-solution-f01p/
'''

class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        left = [1] * N
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        
        ans, right = 0, 1
        for i in range(N - 1, -1, -1):
            if i < N - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
                
            ans += max(left[i], right)
        
        return ans


'''
approach: Greedy
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 99.31 % of python3 submissions.
You are here!
Your memory usage beats 45.17 % of python3 submissions.
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        ans = 1
        inc, dec, pre = 1, 0, 1
        for i in range(1, N):
            if ratings[i] >= ratings[i -1]:
                dec = 0
                pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
                ans += pre
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                ans += dec
                pre = 1
            
        return ans
