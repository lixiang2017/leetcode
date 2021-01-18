'''
Time: O(N + N) ＝ O(N)
Space: O(1)

执行结果：通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了75.00%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了22.06%的用户
'''


class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        zero = one = 0
        for student in students:
            if student:
                one += 1
            else:
                zero += 1
        
        prefer = True
        while prefer and sandwiches:
            prefer = False
            flavour = sandwiches.pop(0)
            if flavour:
                if one:
                    prefer = True
                    one -= 1
            else:
                if zero:
                    prefer = True
                    zero -= 1

        return zero + one
