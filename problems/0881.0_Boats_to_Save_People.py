'''
sort + two pointers
T: O(NlogN + N)
S: O(logN), for quick sort

Runtime: 702 ms, faster than 30.04% of Python3 online submissions for Boats to Save People.
Memory Usage: 20.9 MB, less than 80.59% of Python3 online submissions for Boats to Save People.
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        n = len(people)
        i, j = 0, n - 1
        while i <= j:
            if i != j:
                s = people[i] + people[j]
            else:
                s = people[i]
            if s <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            boats += 1
            
        return boats
    

'''
sort + two pointers
T: O(NlogN + N)
S: O(logN), for quick sort

Runtime: 525 ms, faster than 69.22% of Python3 online submissions for Boats to Save People.
Memory Usage: 21 MB, less than 10.26% of Python3 online submissions for Boats to Save People.
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        n = len(people)
        i, j = 0, n - 1
        while i < j:
            s = people[i] + people[j]
            if s <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            boats += 1
            
        return boats + bool(i == j)

'''
sort + two pointers

Runtime: 640 ms, faster than 43.99% of Python3 online submissions for Boats to Save People.
Memory Usage: 20.9 MB, less than 80.59% of Python3 online submissions for Boats to Save People.
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1
        return i 



'''
sort + two pointers

Runtime: 554 ms, faster than 61.74% of Python3 online submissions for Boats to Save People.
Memory Usage: 20.9 MB, less than 34.38% of Python3 online submissions for Boats to Save People.
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans 
