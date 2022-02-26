'''
Runtime: 33 ms, faster than 70.95% of Python3 online submissions for Compare Version Numbers.
Memory Usage: 13.8 MB, less than 92.33% of Python3 online submissions for Compare Version Numbers.
'''
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = self.parseVersion(version1), self.parseVersion(version2)
        n1, n2 = len(v1), len(v2)
        v1 += (max(n1, n2) - n1) * [0]
        v2 += (max(n1, n2) - n2) * [0]
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:  
            return 0
    
    def parseVersion(self, version: str) -> List[int]:
        return list(map(int, version.split('.')))
        

'''
Runtime: 61 ms, faster than 9.59% of Python3 online submissions for Compare Version Numbers.
Memory Usage: 13.7 MB, less than 99.63% of Python3 online submissions for Compare Version Numbers.
'''
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = self.parseVersion(version1), self.parseVersion(version2)
        n1, n2 = len(v1), len(v2)
        v1 += (max(n1, n2) - n1) * [0]
        v2 += (max(n1, n2) - n2) * [0]
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:  
            return 0
    
    def parseVersion(self, version: str) -> List[int]:
        v = list(map(int, version.split('.')))
        while v and v[-1] == 0:
            v.pop()
        return v

'''
Runtime: 40 ms, faster than 57.81% of Python3 online submissions for Compare Version Numbers.
Memory Usage: 13.8 MB, less than 92.33% of Python3 online submissions for Compare Version Numbers.
'''
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        for vv1, vv2 in zip_longest(v1, v2, fillvalue=0):
            if vv1 < vv2:
                return -1
            elif vv1 > vv2:
                return 1
        return 0

'''
Runtime: 30 ms, faster than 85.36% of Python3 online submissions for Compare Version Numbers.
Memory Usage: 13.9 MB, less than 92.33% of Python3 online submissions for Compare Version Numbers.
'''
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        for vv1, vv2 in zip_longest(v1, v2, fillvalue=0):
            if vv1 < vv2:
                return -1
            elif vv1 > vv2:
                return 1
        return 0




        