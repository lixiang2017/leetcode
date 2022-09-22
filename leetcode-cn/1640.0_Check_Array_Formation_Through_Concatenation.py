'''
approach: Hash Table
Time: O(N + N) = O(N)
Space: O(N + N) = O(N)

执行用时：20 ms, 在所有 Python 提交中击败了75.70% 的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了77.57% 的用户
'''


class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        # element to position
        ele2pos = {ele: i for i, ele in enumerate(arr)}
        N = len(arr)

        found = 0
        for piece in pieces:
            pLen = len(piece)
            head = piece[0]
            if head not in ele2pos:
                return False
            start = ele2pos[head]
            if piece != arr[start : start + pLen]:
                return False
            else:
                found += pLen
                
        return found == N



'''
Time: O(N^2)
Space: O(N)

执行用时：16 ms, 在所有 Python 提交中击败了91.59% 的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了16.82% 的用户

ref:
https://leetcode-cn.com/problems/check-array-formation-through-concatenation/solution/6xing-dai-ma-jie-jue-wen-ti-chao-jian-yi-pythonjie/
'''

class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        concate = []
        for element in arr:
            for piece in pieces:
                if element == piece[0]:
                    concate += piece
        return concate == arr



'''
Time: O(N^2)
Space: O(N)

执行用时：20 ms, 在所有 Python 提交中击败了75.70% 的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了77.57% 的用户
'''

class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        # use 1. sum(pieces[i].length) == arr.length and 2. distinct
        for piece in pieces:
            if piece[0] not in arr:
                return False
            startIdx = arr.index(piece[0])
            if piece != arr[startIdx: startIdx + len(piece)]:
                return False
        return True


'''
执行用时：36 ms, 在所有 Python3 提交中击败了80.00% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了92.68% 的用户
通过测试用例：84 / 84
'''
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pos = {x : i for i, x in enumerate(arr)}
        for piece in pieces:
            pre_idx = None 
            for x in piece:
                if x not in pos or (pre_idx is not None and pre_idx + 1 != pos[x]):
                    return False
                pre_idx = pos[x]
        return True
        