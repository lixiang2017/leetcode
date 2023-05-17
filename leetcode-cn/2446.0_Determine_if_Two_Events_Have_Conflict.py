'''
执行用时：48 ms, 在所有 Python3 提交中击败了15.17% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了20.79% 的用户
通过测试用例：129 / 129
'''
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def strTime2Int(strTime):
            h, m = map(int, strTime.split(':'))
            return h * 60 + m 

        st1, et1 = map(strTime2Int, event1)
        st2, et2 = map(strTime2Int, event2)
        if et1 < st2 or et2 < st1:
            return False
        return True

'''
执行用时：40 ms, 在所有 Python3 提交中击败了45.51% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了25.84% 的用户
通过测试用例：129 / 129
'''
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def strTime2Int(strTime):
            h, m = map(int, strTime.split(':'))
            return h * 60 + m 

        st1, et1 = map(strTime2Int, event1)
        st2, et2 = map(strTime2Int, event2)
        return not (et1 < st2 or et2 < st1)

