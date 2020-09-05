


import itertools
class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        max_time = -1
        # enumerate all possibilities, with permutation() function
        for h, i, j, k in itertools.permutations(arr):
            hour = h * 10 + i
            minute = j * 10 + k
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)
        
        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)
        


if __name__ == '__main__':
	A = [1,2,3,4]
	assert Solution().largestTimeFromDigits(A) == "23:41"

	A = [5,5,5,5]
	assert Solution().largestTimeFromDigits(A) == ""

	A = [0,0,0,0]
	assert Solution().largestTimeFromDigits(A) == "00:00"

	A = [0,0,1,0]
	assert Solution().largestTimeFromDigits(A) == "10:00"
