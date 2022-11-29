'''
Runtime: 5182 ms, faster than 11.96% of Python3 online submissions for Find Players With Zero or One Losses.
Memory Usage: 69.8 MB, less than 16.89% of Python3 online submissions for Find Players With Zero or One Losses.
'''
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win, lose = Counter(), Counter()
        player = set()
        for w, l in matches:
            win[w] += 1
            lose[l] += 1
            player.add(w)
            player.add(l)
            
        not_lost = []
        lost_one = []
        player = sorted(player)
        for p in player:
            if p not in lose:
                not_lost.append(p)
            if lose[p] == 1:
                lost_one.append(p)
        return [not_lost, lost_one]
        
        