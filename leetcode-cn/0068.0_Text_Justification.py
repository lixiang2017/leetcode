'''
Simulation
T: O(N)
S: O(N)

执行用时：24 ms, 在所有 Python3 提交中击败了96.93% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了86.18% 的用户
通过测试用例：27 / 27
'''
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        # one line words
        ws = []
        # one line len
        one_len = 0
        ws_cnt = 0
        for w in words:
            if one_len + len(w) <= maxWidth:
                ws.append(w)
                one_len += 1 + len(w)
                ws_cnt += 1
            else:
                space = maxWidth - (one_len - ws_cnt)
                if ws_cnt > 1:
                    q, remainder = divmod(space, ws_cnt - 1)
                    one_line = ''
                    i = 0
                    for _ in range(remainder):
                        one_line += ws[i]
                        one_line += ' ' * (1 + q)
                        i += 1                        
                    while i < ws_cnt - 1:
                        one_line += ws[i]
                        one_line += ' ' * (q)
                        i += 1
                    one_line += ws[i]
                    ans.append(one_line)
                else:  # == 1
                    ans.append(ws[0] + ' ' * (maxWidth - one_len + 1) )

                # next
                ws = [w]
                one_len = len(w) + 1
                ws_cnt = 1

        if ws:
            one_line = ' '.join(ws)
            one_line += ' ' * (maxWidth - len(one_line))
            ans.append(one_line)
        else:
            one_line = ' '.join(ans[-1].split())
            one_line += ' ' * (maxWidth - len(one_line))
            ans[-1] = one_line
        return ans
