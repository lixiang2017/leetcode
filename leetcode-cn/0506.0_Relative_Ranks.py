'''
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
        
        