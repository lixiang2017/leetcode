'''
看题目限制 1 <= tops[i], bottoms[i] <= 6, 只可能range(1, 7)
T: O(6 * N)
S: O(1)

Runtime: 1458 ms, faster than 51.81% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
Memory Usage: 15.2 MB, less than 44.98% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
'''
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        ans = n + 5
        for v in range(1, 7):
            t = b = 0
            can_do = True
            for i in range(n):             
                # try tops
                if tops[i] != v and bottoms[i] != v:
                    can_do = False
                    break
                elif tops[i] != v:
                    t += 1
                # try bottoms
                elif bottoms[i] != v:
                    b += 1
    
            if can_do:
                ans = min(ans, t, b)
        
        return ans if ans != n + 5 else -1
    
        
'''
其实最终选择的数，只可能tops[0]和bottoms[0]两种情况。
T: O(2 * N)
S: O(1)


Runtime: 1401 ms, faster than 57.91% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
Memory Usage: 15.2 MB, less than 22.57% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
'''
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        ans = n + 5
        for v in [tops[0], bottoms[0]]:
            t = b = 0
            can_do = True
            for i in range(n):             
                # try tops
                if tops[i] != v and bottoms[i] != v:
                    can_do = False
                    break
                elif tops[i] != v:
                    t += 1
                # try bottoms
                elif bottoms[i] != v:
                    b += 1
    
            if can_do:
                ans = min(ans, t, b)
        
        return ans if ans != n + 5 else -1
  

'''
ref:
https://leetcode-cn.com/problems/minimum-domino-rotations-for-equal-row/comments/
T: 一次O(N)遍历+一次常数级遍历O(6)
S: O(7 * 3)

思路：遍历A和B，分别统计up和down的对应点数的个数，若上下相同则可以踢掉，该点对应的总长度减去1，反之分别累加上下对应点数的次数
遍历1-6点数，找出这六个点数的up和down中的最小值就是答案


Runtime: 1216 ms, faster than 80.89% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
Memory Usage: 15.1 MB, less than 77.02% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
'''

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        up, down, need = Counter(), Counter(), [n] * 7
        for i in range(n):
            if tops[i] == bottoms[i]:
                need[tops[i]] -= 1
            else:
                up[tops[i]] += 1
                down[bottoms[i]] += 1
                
        ans = n + 5
        for v in range(1, 7):
            if up[v] + down[v] < need[v]:
                continue
            ans = min(ans, min(up[v], down[v]))
        
        return ans if ans != n + 5 else -1

'''
可能Python3 对于自己的迭代有优化，居然这么快。
T: O(2 * N)
S: O(1)

Runtime: 1088 ms, faster than 98.11% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
Memory Usage: 15.3 MB, less than 11.37% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
'''
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for candidate in (tops[0], bottoms[0]):
            if all(candidate in pair for pair in zip(tops, bottoms)):
                return len(tops) - max(tops.count(candidate), bottoms.count(candidate))
        return -1
                



