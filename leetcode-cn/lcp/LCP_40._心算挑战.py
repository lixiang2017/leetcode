'''
432ms 击败38.46%
25.68MB 击败65.39%
'''
class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort()
        n = len(cards)
        s = sum(cards[n - cnt: ])
        min_odd = min_even = 1005
        for i in range(n - 1, n - cnt - 1, -1):
            if cards[i] % 2:
                min_odd = min(min_odd, cards[i])
            else:
                min_even = min(min_even, cards[i])

        if s % 2 == 0:
            return s 

        i = n - cnt - 1
        while s % 2 != 0 and i >= 0:
            if cards[i] % 2 == 0 and min_odd != 1005:
                return s - (min_odd - cards[i])
            if cards[i] % 2 == 1 and min_even != 1005:
                return s - (min_even - cards[i])
            i -= 1
        return 0


class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort()
        n = len(cards)
        s = sum(cards[n - cnt: ])
        min_odd = min_even = 1005
        for i in range(n - 1, n - cnt - 1, -1):
            if cards[i] % 2:
                min_odd = min(min_odd, cards[i])
            else:
                min_even = min(min_even, cards[i])

        i = n - cnt - 1
        while s % 2 != 0 and i >= 0:
            if cards[i] % 2 == 0 and min_odd != 1005:
                return s - (min_odd - cards[i])
            if cards[i] % 2 == 1 and min_even != 1005:
                return s - (min_even - cards[i])
            i -= 1
        return 0 if s % 2 else s


'''
0x3f
'''
class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        s = sum(cards[: cnt])
        if s % 2 == 0:
            return s 
        
        def replace_sum(x: int) -> int:
            for v in cards[cnt: ]:
                if v % 2 != x % 2:
                    return s - x + v
            return 0
        
        x = cards[cnt - 1]
        ans = replace_sum(x)
        for v in cards[cnt - 1:: -1]:
            if v % 2 != x % 2:
                ans = max(ans, replace_sum(v))
                break 
        return ans 


