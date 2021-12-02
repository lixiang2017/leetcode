'''
计数排序
hash table

执行用时：52 ms, 在所有 Python3 提交中击败了33.69% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了5.10% 的用户
通过测试用例：17 / 17
'''
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        L = max(score) + 1
        has = [0] * L
        for s in score:
            has[s] = 1
        medal = {
            1: 'Gold Medal',
            2: 'Silver Medal',
            3: 'Bronze Medal',
        }
        rank = [0] * L
        r = 0
        for i in range(L - 1, -1, -1):
            if has[i] == 1:
                r += 1
                rank[i] = medal.get(r, str(r))
        
        return [rank[s] for s in score]
        
'''
heap
执行用时：44 ms, 在所有 Python3 提交中击败了52.21% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了52.35% 的用户
通过测试用例：17 / 17
'''
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        h = []
        for i, s in enumerate(score):
            heappush(h, (-s, i))
        medal = {
            1: 'Gold Medal',
            2: 'Silver Medal',
            3: 'Bronze Medal', 
        }
        rank = 1
        while h:
            neg_s, idx = heappop(h)
            score[idx] = medal.get(rank, str(rank))
            rank += 1
        return score

'''
计数排序

执行用时：48 ms, 在所有 Python3 提交中击败了37.72% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了84.30% 的用户
通过测试用例：17 / 17
'''
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medal = {
            1: 'Gold Medal',
            2: 'Silver Medal',
            3: 'Bronze Medal', 
        }
        maxs = max(score)
        score_idx = [-1] * (maxs + 1)
        for i, s in enumerate(score):
            score_idx[s] = i 
        rank = 1
        while maxs >= 0:
            if score_idx[maxs] >= 0:
                score[score_idx[maxs]] = medal.get(rank, f'{rank}')
                rank += 1
            maxs -= 1

        return score

     
'''
执行用时：40 ms, 在所有 Python3 提交中击败了71.54% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了45.10% 的用户
通过测试用例：17 / 17
'''
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medal = ('Gold Medal', 'Silver Medal', 'Bronze Medal')
        location = dict()
        for i, s in enumerate(score):
            location[s] = i 
        score.sort(reverse=True)
        ans = [0] * len(score)
        for i, s in enumerate(score):
            if i < 3:
                ans[location[s]] = medal[i]
            else:
                ans[location[s]] = str(i + 1)
        return ans
        
