'''
21 / 32 test cases passed.
	Status: Time Limit Exceeded
	
'''

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        def check(w1, w2):
            diff = 0
            for ch1, ch2 in zip(w1, w2):
                if ch1 != ch2:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        
        q = deque([
            ([beginWord], set([beginWord]) )
        ])  # (seq, visited), ...
        while q:
            N = len(q)
            for _ in range(N):
                seq, visited = q.popleft()
                seen = visited.copy() 

                for word in wordList:
                    if word not in seen:
                        if check(seq[-1], word):
                            seen.add(word)
                            q.append((seq + [word], seen))
            # check every sequence in the q
            Found = any(True if seq[-1] == endWord else False for seq, seen in q)
            if Found:
                return [seq for seq, seen in q if seq[-1] == endWord]
        
        return []


'''
approach: BFS + Hash Set
visited set: last level
seen set: current level

You are here!
Your runtime beats 10.34 % of python3 submissions.
You are here!
Your memory usage beats 55.21 % of python3 submissions.
'''
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        def check(w1, w2):
            diff = 0
            for ch1, ch2 in zip(w1, w2):
                if ch1 != ch2:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        
        q = deque([
            [beginWord]
        ])  # (seq, visited), ...
        visited = set([beginWord])
        while q:
            N = len(q)
            ans = []
            seen = visited.copy() 
            for _ in range(N):
                seq = q.popleft()
                
                for word in wordList:
                    if word not in visited:
                        if check(seq[-1], word):
                            seen.add(word)
                            q.append(seq + [word])
                            if word == endWord:
                                ans.append(seq + [word])
            visited = seen.copy()
            if ans:
                return ans
        
        return []
 