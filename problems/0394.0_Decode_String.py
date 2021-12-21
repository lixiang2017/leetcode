'''
Runtime: 24 ms, faster than 95.62% of Python3 online submissions for Decode String.
Memory Usage: 14.2 MB, less than 79.98% of Python3 online submissions for Decode String.
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_string = ''
        for ch in s:
            if ch == '[':
                stack.append(cur_string)
                stack.append(cur_num)
                cur_string = ''
                cur_num = 0
            elif ch == ']':
                n = stack.pop()
                prev_string = stack.pop()
                cur_string = prev_string + cur_string * n
            elif ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            else:
                cur_string += ch
        
        return cur_string
