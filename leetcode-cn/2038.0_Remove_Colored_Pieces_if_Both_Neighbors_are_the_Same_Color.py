'''
T: O(N)
S: O(1)

执行用时：112 ms, 在所有 Python3 提交中击败了98.98% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了28.57% 的用户
通过测试用例：83 / 83
'''
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a, b, pre = 0, 0, None
        part_a = part_b = 0
        for ch in colors:    
            if ch == pre:
                if ch == 'A':
                    part_a += 1
                else:
                    part_b += 1
            else:
                if ch == 'A':
                    if part_b >= 3:
                        b += part_b - 2
                    pre = 'A'
                    part_a = 1
                else:
                    if part_a >= 3:
                        a += part_a - 2
                    pre = 'B'
                    part_b = 1 

        # do not forget last part!!!
        if pre == 'A' and part_a >= 3:
            a += part_a - 2
        if pre == 'B' and part_b >= 3:
            b += part_b - 2   
      
        return a > b 


'''
T: O(N)
S: O(1)

执行用时：220 ms, 在所有 Python3 提交中击败了52.04% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了55.10% 的用户
通过测试用例：83 / 83
'''
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = b = 0
        n = len(colors)
        for i in range(n - 2): # n-3 +2
            # i, i + 1, i + 2
            part = colors[i: i + 3]
            if part == "AAA":
                a += 1
            elif part == "BBB":
                b += 1
     
        return a > b 

'''
执行用时：240 ms, 在所有 Python3 提交中击败了47.96% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了45.92% 的用户
通过测试用例：83 / 83
'''
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = b = 0
        n, c = len(colors), colors
        for i in range(n - 2): # n-3 +2
            # i, i + 1, i + 2
            if c[i] == 'A' and c[i + 1] == 'A' and c[i + 2] == 'A':
                a += 1
            elif c[i] == 'B' and c[i + 1] == 'B' and c[i + 2] == 'B':
                b += 1
     
        return a > b 

        
