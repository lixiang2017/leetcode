'''
Two Pointers
Time: O(N)
Space: O(1)

执行用时：24 ms, 在所有 Python3 提交中击败了99.22% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了22.22% 的用户
'''
class Solution:
    def compress(self, chars: List[str]) -> int:
        pre, repeat, i = '', 0, 0
        for idx, ch in enumerate(chars):
            if ch == pre:
                repeat += 1
            else:
                if 0 == repeat:
                    repeat = 1
                    pre = ch
                    continue
                elif 1 == repeat:
                    chars[i] = pre
                    i += 1
                else:
                    chars[i] = pre
                    i += 1
                    L = len(str(repeat))
                    chars[i: i + L] = list(str(repeat))
                    i += L
                pre = ch
                repeat = 1
        # end
        if 1 == repeat:
            chars[i] = pre
            i += 1
        else:
            chars[i] = pre
            i += 1
            L = len(str(repeat))
            chars[i: i + L] = list(str(repeat))
            i += L 

        return i
        