'''
Runtime: 37 ms, faster than 68.69% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
Memory Usage: 16.2 MB, less than 39.54% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
'''
class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)
        
        