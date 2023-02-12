'''
hash table + simulation

执行用时：48 ms, 在所有 Python3 提交中击败了22.00% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了34.00% 的用户
通过测试用例：61 / 61
'''
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        ch2pos = {}
        for ch in string.ascii_lowercase:
            idx = ord(ch) - ord('a')
            x, y = divmod(idx, 5)
            ch2pos[ch] = (x, y)
        seq = []

        def move_vertically(dx):
            if dx > 0:
                seq.append('D' * dx)
            else:
                seq.append('U' * (-dx))
        
        def move_horizontally(dy):
            if dy > 0:
                seq.append('R' * dy)
            else:
                seq.append('L' * (-dy))
        # prev
        px, py = 0, 0
        pre_ch = ''
        for ch in target:
            x, y = ch2pos[ch]
            dx, dy = x - px, y - py 
            if pre_ch == 'z':
                move_vertically(dx)
                move_horizontally(dy)
            else:
                move_horizontally(dy)
                move_vertically(dx)                   
            seq.append('!')
            px, py = x, y
            pre_ch = ch 
        return ''.join(seq)

'''
四个方向 只需保证 "先上再右，先左再下" 即可
所以，U、L可以互换，R、D可以互换。

执行用时：28 ms, 在所有 Python3 提交中击败了94.00% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了74.00% 的用户
通过测试用例：61 / 61
'''
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        i = j = 0
        ans = ''
        for ch in target:
            row, col = divmod(ord(ch) - ord('a'), 5)
            while i > row:
                i -= 1
                ans += 'U'
            while j > col:
                j -= 1
                ans += 'L'
            while j < col:
                j += 1
                ans += 'R'
            while i < row:
                i += 1
                ans += 'D'
            ans += '!'
        return ans 
