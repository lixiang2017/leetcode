'''
approach: Two pointers
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 61.85 % of python submissions.
You are here!
Your memory usage beats 68.21 % of python submissions.
'''


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boats = 0
        people.sort()
        size = len(people)
        i, j = 0, size - 1
        while i < j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
                boats += 1
            else:
                j -= 1
                boats += 1
                
        if i == j: boats +=1 
            
        return boats
