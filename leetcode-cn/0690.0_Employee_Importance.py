'''
approach: Hash Table + Queue/BFS
Time: O(N)
Space: O(N)

执行用时：168 ms, 在所有 Python3 提交中击败了54.94%的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了40.11%的用户
'''


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total = 0
        id2employee = {employee.id: employee for employee in employees}
        queue = [id]
        while queue:
            employee_id = queue.pop(0)
            total += id2employee[employee_id].importance
            queue.extend(id2employee[employee_id].subordinates)

        return total



'''
approach: Hash Table + DFS
Time: O(N)
Space: O(N)

执行用时：184 ms, 在所有 Python3 提交中击败了35.90%的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了15.56%的用户
'''

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        id2employee = {employee.id: employee for employee in employees}
        def dfs(id):
            total = 0
            total += id2employee[id].importance
            subs = id2employee[id].subordinates
            if subs:
                for sub in subs:
                    total += dfs(sub)
            return total

        return dfs(id)
