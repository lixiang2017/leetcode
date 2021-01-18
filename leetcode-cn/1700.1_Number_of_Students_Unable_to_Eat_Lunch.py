'''
no need for "prefer" to keep status

执行结果：通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了88.24%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了25.00%的用户
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
        
        while sandwiches:
            flavour = sandwiches.pop(0)
            if flavour:
                if one:
                    one -= 1
                else:
                    break
            else:
                if zero:
                    zero -= 1
                else:
                    break

        return zero + one
