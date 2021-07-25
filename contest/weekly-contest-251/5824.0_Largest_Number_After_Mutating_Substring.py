'''
Time: O(N)
Space: O(N)

执行用时：244 ms, 在所有 Python3 提交中击败了25.00% 的用户
内存消耗：22.3 MB, 在所有 Python3 提交中击败了25.00% 的用户
'''
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        N = len(num)
        mutating, i = [], 0
        # header
        while i < N and change[int(num[i])] <= int(num[i]):
            mutating.append(num[i])
            i += 1
        
        while i < N and change[int(num[i])] >= int(num[i]):
            mutating.append(str(change[int(num[i])]))
            i += 1            
        
        # tail
        if i < N:
            mutating += num[i:]
        
        return ''.join(mutating)

'''
输入："214010"
[6,7,9,7,4,0,3,4,4,7]
输出："974010"
预期："974676"

中间的4也是替换
'''

