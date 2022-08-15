'''
BFS

Runtime: 213 ms, faster than 14.19% of Python3 online submissions for Word Ladder II.
Memory Usage: 14.6 MB, less than 71.47% of Python3 online submissions for Word Ladder II.

2022-08-14 测试用例增强了， 现在会 TLE
'''
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set()
        for word in wordList:
            word_set.add(word)
        if endWord not in word_set:
            return []
        
        q = deque([ [beginWord, [beginWord]] ])   
        l = len(beginWord)
        seen = set([beginWord])
        while q:
            next_q = deque()
            ans = []
            visited = seen.copy()
            for word, arr in q:
                for i in range(l):
                    for low in string.ascii_lowercase:
                        com = word[: i] + low + word[i + 1: ]
                        if com in word_set:
                            if com == endWord:
                                ans.append(arr + [com])
                            else:
                                if com not in visited:
                                    next_q.append([com, arr + [com]])
                                    seen.add(com)
            if ans:
                return ans
            else:
                q = next_q

        return []    



'''
先使用 BFS 找到最短路径的长度，再使用 DFS + memo 寻找路径。

Runtime: 246 ms, faster than 20.77% of Python3 online submissions for Word Ladder II.
Memory Usage: 18.8 MB, less than 6.57% of Python3 online submissions for Word Ladder II.
'''
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []

        graph = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                key = w[: i] + '?' + w[i + 1: ]
                graph[key].append(w)

        def depth() -> int:
            d = 0
            seen = {beginWord}
            q = deque([beginWord])
            while q:
                for _ in range(len(q)):
                    w = q.popleft()
                    for i in range(len(w)):
                        key = w[: i] + '?' + w[i + 1: ]
                        for neigh in graph[key]:
                            if neigh == endWord:
                                return d + 1
                            if neigh not in seen:
                                seen.add(neigh)
                                q.append(neigh)
                d += 1
            return -1

        d = depth()
        if -1 == d:
            return []

        @lru_cache(None)
        def walk(word, d):
            if 0 == d:
                if word == endWord:
                    return [[endWord]]
                return []

            result = []
            for i in range(len(word)):
                key = word[: i] + '?' + word[i + 1: ]
                for neigh in graph[key]:
                    paths = walk(neigh, d - 1)
                    result += [[word] + path for path in paths]
            return result 

        return walk(beginWord, d)


