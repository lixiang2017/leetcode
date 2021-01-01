'''
You are here!
Your runtime beats 100.00 % of python submissions.
'''



class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        records = [0] * 1000
        for (num, start, end) in trips:
        	records[start] += num
        	records[end] -= num

        curNum = 0 
        for record in records:
        	curNum += record
        	if curNum > capacity:
        		return False

        return True


if __name__ == '__main__':
	trips = [[2,1,5],[3,3,7]]
	capacity = 4
	assert not Solution().carPooling(trips, capacity)

	trips = [[2,1,5],[3,3,7]]
	capacity = 5
	assert Solution().carPooling(trips, capacity)

	trips = [[2,1,5],[3,5,7]]
	capacity = 3
	assert Solution().carPooling(trips, capacity)

	trips = [[3,2,7],[3,7,9],[8,3,9]]
	capacity = 11
	assert Solution().carPooling(trips, capacity)


