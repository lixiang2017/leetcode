'''
prefix sum + postfix sum
T: O(3 * k) = O(k)
S: O(2 * K) = O(k)

Runtime: 451 ms, faster than 88.96% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
Memory Usage: 28.2 MB, less than 5.40% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k >= n:
            return sum(cardPoints)
        pre, post = [0], [0]
        for i in range(k):
            pre.append(pre[-1] + cardPoints[i])
        for i in range(n - 1, n - k - 1, -1):
            post.append(post[-1] + cardPoints[i])
        return max(pre[i] + post[k - i] for i in range(k + 1))


'''
remove if k >= n

Runtime: 428 ms, faster than 96.90% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
Memory Usage: 28.1 MB, less than 5.40% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        pre, post = [0], [0]
        for i in range(k):
            pre.append(pre[-1] + cardPoints[i])
        for i in range(n - 1, n - k - 1, -1):
            post.append(post[-1] + cardPoints[i])
        return max(pre[i] + post[k - i] for i in range(k + 1))

'''
sliding window
T: O(N)
S: O(1)

Runtime: 763 ms, faster than 18.40% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
Memory Usage: 27.3 MB, less than 71.96% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n, s = len(cardPoints), sum(cardPoints)
        # middle sum for sliding window
        i = middle = 0
        while i < n - k:
            middle += cardPoints[i]
            i += 1
        ans = s - middle
        for i in range(n - k, n):
            middle += cardPoints[i] - cardPoints[i - (n-k)]
            ans = max(ans, s - middle)
        return ans 


'''
s - min_middle

Runtime: 730 ms, faster than 22.78% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
Memory Usage: 27.4 MB, less than 60.88% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n, s = len(cardPoints), sum(cardPoints)
        # middle sum for sliding window
        i = middle = 0
        while i < n - k:
            middle += cardPoints[i]
            i += 1
        min_middle = middle
        for i in range(n - k, n):
            middle += cardPoints[i] - cardPoints[i - (n-k)]
            min_middle = min(min_middle, middle)
        return s - min_middle


'''
# s = sum(cardPoints)
过程中计算总和

Runtime: 464 ms, faster than 83.33% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
Memory Usage: 27.4 MB, less than 40.17% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # s = sum(cardPoints)
        s = 0
        # middle sum for sliding window
        i = middle = 0
        while i < n - k:
            middle += cardPoints[i]
            i += 1
        min_middle = s = middle
        for i in range(n - k, n):
            s += cardPoints[i]
            middle += cardPoints[i] - cardPoints[i - (n-k)]
            min_middle = min(min_middle, middle)
        return s - min_middle



'''
把上面两种方法结合起来，取时间复杂度最小的

Runtime: 448 ms, faster than 90.51% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
Memory Usage: 27.2 MB, less than 80.27% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if 3 * k <= n:
            pre, post = [0], [0]
            for i in range(k):
                pre.append(pre[-1] + cardPoints[i])
            for i in range(n - 1, n - k - 1, -1):
                post.append(post[-1] + cardPoints[i])
            return max(pre[i] + post[k - i] for i in range(k + 1))
        else:  
            # s = sum(cardPoints)
            s = 0
            # middle sum for sliding window
            i = middle = 0
            while i < n - k:
                middle += cardPoints[i]
                i += 1
            min_middle = s = middle
            for i in range(n - k, n):
                s += cardPoints[i]
                middle += cardPoints[i] - cardPoints[i - (n-k)]
                min_middle = min(min_middle, middle)
            return s - min_middle



