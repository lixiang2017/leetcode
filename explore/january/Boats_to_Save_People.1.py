'''
approach: Two pointers
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 39.31 % of python submissions.
You are here!
Your memory usage beats 14.45 % of python submissions.
'''

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1
        return i
