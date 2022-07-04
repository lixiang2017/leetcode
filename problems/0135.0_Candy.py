'''
heap / sort
T: O(NlogN)
S: O(N)

Runtime: 274 ms, faster than 38.19% of Python3 online submissions for Candy.
Memory Usage: 18.4 MB, less than 6.62% of Python3 online submissions for Candy.
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n 
        h = [(r, i) for i, r in enumerate(ratings)]
        heapify(h)
        while h:
            r, i = heappop(h)
            c = 1
            # left
            if 0 <= i - 1 < n and ratings[i - 1] < ratings[i]:
                c = max(c, candy[i - 1] + 1)
            # right 
            if 0 <= i + 1 < n and ratings[i + 1] < ratings[i]:
                c = max(c, candy[i + 1] + 1)
            candy[i] = c 
        return sum(candy)

'''
sort
T: O(NlogN)
S: O(N)

Runtime: 362 ms, faster than 10.78% of Python3 online submissions for Candy.
Memory Usage: 18 MB, less than 8.19% of Python3 online submissions for Candy.
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n 
        rs = [(r, i) for i, r in enumerate(ratings)]
        rs.sort()
        for r, i in rs:
            c = 1
            # left
            if 0 <= i - 1 < n and ratings[i - 1] < ratings[i]:
                c = max(c, candy[i - 1] + 1)
            # right 
            if 0 <= i + 1 < n and ratings[i + 1] < ratings[i]:
                c = max(c, candy[i + 1] + 1)
            candy[i] = c 
        return sum(candy)
