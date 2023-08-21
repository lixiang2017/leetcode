'''
时间 216ms, 击败 55.22%使用 Python3 的用户
内存 16.42MB, 击败 58.21%使用 Python3 的用户
'''
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        if start.replace('_', '') != target.replace('_', ''):
            return False
        i = j = 0
        while i < n and j < n:
            if 'L' == target[j]:
                while i < n and start[i] == '_':
                    i += 1
                if i < j or start[i] != 'L':
                    return False
                else:
                    i += 1
            if 'R' == target[j]:
                while i < n and start[i] == '_':
                    i += 1
                if i > j or start[i] != 'R':
                    return False 
                else:
                    i += 1
            j += 1

        return True 
