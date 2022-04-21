'''
stack
T: O(N)
S: O(N)

执行用时：28 ms, 在所有 Python3 提交中击败了97.28% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了66.15% 的用户
通过测试用例：26 / 26
'''
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        ans, stack = 0, []
        curr_len = 0
        for layer in input.split('\n'):
            tab_cnt = 0
            i, l = 0, len(layer)
            while i < l and layer[i: i + 1] == u'\t':
                tab_cnt += 1
                i += 1
            dir_file = layer[i: ]
            while len(stack) > tab_cnt:
                curr_len -= len(stack[-1])
                stack.pop()  
            stack.append(dir_file) 
            curr_len += len(stack[-1])   
            if '.' in dir_file:
                # len(stack) - 1 count for / / / / 
                ans = max(ans, curr_len + len(stack) - 1)

        return ans 



'''
执行用时：44 ms, 在所有 Python3 提交中击败了14.01% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了63.04% 的用户
通过测试用例：26 / 26
'''
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        ans, stack = 0, []
        curr_len = 0
        for layer in input.split('\n'):
            dir_file = layer.lstrip('\t')
            tab_cnt = len(layer) - len(dir_file)
            while len(stack) > tab_cnt:
                curr_len -= len(stack[-1])
                stack.pop()  
            stack.append(dir_file) 
            curr_len += len(stack[-1])   
            if '.' in dir_file:
                # len(stack) - 1 count for / / / / 
                ans = max(ans, curr_len + len(stack) - 1)
        return ans 


