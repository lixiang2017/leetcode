'''
You are here!
Your runtime beats 68.32 % of python submissions.
'''


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        size = len(seats)
        i = 0
        while i < size and not seats[i]:
            i += 1
        leading = i

        j = size - 1
        while j >= 0 and not seats[j]:
            j -= 1
        trailing = size - 1 - j
        # for k in range(i, j + 1):
        mids = ''.join([str(seat) for seat in seats[i: j + 1]]).split('1')
        mid_distance = max([(len(mid) + 1) / 2 for mid in mids])
        return max(leading, mid_distance, trailing)
