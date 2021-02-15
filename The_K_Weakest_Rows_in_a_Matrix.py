'''
approach: Sort
Time: O(M * N + MlogM)
Space: O(M)

You are here!
Your runtime beats 84.57 % of python submissions.
'''


class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        soldiers = [(i, sum(m)) for i, m in enumerate(mat)]
        soldiers.sort(key=lambda soldier: (soldier[1], soldier[0]))
        return [i for i, soldier in soldiers[: k]]
