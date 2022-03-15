'''
hash table + heap

感想：
有时候直接看答案的思路和代码，并没有自己中间的探索过程、排错过程。
往往这些排错过程更能让自己成长，也更能明白最后的答案、最优的答案为何这样写。

执行用时：32 ms, 在所有 Python3 提交中击败了84.37% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了57.41% 的用户
通过测试用例：16 / 16
'''
class Twitter:

    def __init__(self):
        # followerId -> followeeId set
        self.guest2hosts = defaultdict(set)
        # userId -> posts list or # heap, maybe not need
        self.posts = defaultdict(list)
        # Tweets must be ordered from most recent to least recent.
        self.time_no = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([-self.time_no, tweetId])
        self.time_no += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news = self.posts[userId][:]  # need to make a copy
        for host in self.guest2hosts[userId]:
            news.extend(self.posts[host][-10: ])
        heapify(news)
        feed, cnt = [], 10
        while news and cnt:
            n_time_no, tweetId = heappop(news)
            feed.append(tweetId)
            cnt -= 1
        return feed 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.guest2hosts[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.guest2hosts[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


'''
# error 1
5 / 16 个通过测试用例
状态：解答错误
提交时间：22 分钟前
最后执行的输入：
["Twitter","postTweet","getNewsFeed","follow","getNewsFeed","unfollow","getNewsFeed"]
[[],[1,1],[1],[2,1],[2],[2,1],[2]]

先发动态，后关注，仍需获得之前动态。否则会丢失feed。
所以不能来一个post 就去分发给所有人

# error 2
通过测试用例：9 / 16
输入：
["Twitter","postTweet","postTweet","getNewsFeed"]
[[],[1,5],[1,3],[1]]
输出：
[null,null,null,[5,3]]
预期结果：
[null,null,null,[3,5]]

后发的tweetId 3 要优先于先前发的tweetId 5
'''

