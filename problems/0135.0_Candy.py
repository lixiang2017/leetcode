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


'''
two pass
T: O(3 * N)
S: O(N)

Runtime: 304 ms, faster than 26.40% of Python3 online submissions for Candy.
Memory Usage: 16.8 MB, less than 37.74% of Python3 online submissions for Candy.
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n 
        # from left to right 
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        # from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)
        return sum(candy)


'''
two pass
T: O(2 * N)
S: O(N)

Runtime: 324 ms, faster than 19.79% of Python3 online submissions for Candy.
Memory Usage: 16.7 MB, less than 74.92% of Python3 online submissions for Candy.
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n 
        # from left to right 
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        ans = candy[-1]
        # from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)
            ans += candy[i]
        return ans

'''
DP
T: O(2 * N)
S: O(N)

Runtime: 305 ms, faster than 26.02% of Python3 online submissions for Candy.
Memory Usage: 16.8 MB, less than 37.74% of Python3 online submissions for Candy.
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n 
        # from left to right 
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
                
        ans, right = 0, 1
        # from right to left
        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            ans += max(left[i], right)
        return ans


'''
DP
T: O(N)
S: O(1)

Runtime: 209 ms, faster than 68.75% of Python3 online submissions for Candy.
Memory Usage: 16.8 MB, less than 37.74% of Python3 online submissions for Candy.
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans, inc, dec, prev = 1, 1, 0, 1
        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                prev += 1
                if ratings[i] == ratings[i - 1]:
                    prev = 1
                ans += prev 
                inc = prev 
                dec = 0
            else:
                dec += 1
                if inc == dec:
                    dec += 1
                ans += dec 
                prev = 1
        return ans

