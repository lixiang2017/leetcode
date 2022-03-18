'''
monotonic stack + greedy
T: O(N)
S: O(N)

Runtime: 87 ms, faster than 10.13% of Python3 online submissions for Remove Duplicate Letters.
Memory Usage: 13.9 MB, less than 87.68% of Python3 online submissions for Remove Duplicate Letters.
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        cnt = Counter(s)
        ans_len = len(cnt)
        seen = set()
        for ch in s:
            if ch in seen:
                cnt[ch] -= 1
                continue
            while stack and stack[-1] >= ch and cnt[stack[-1]] > 1:
                cnt[stack[-1]] -= 1
                seen.discard(stack[-1])
                stack.pop()
                
            stack.append(ch)
            seen.add(ch)
            
        return ''.join(stack)[: ans_len]
    
'''
Input
"cdadabcc"
Output
"adab"
Expected
"adbc"

Input
"abacb"
Output
"acb"
Expected
"abc"

Input
"bbcaac"
Output
"ac"
Expected
"bac"
'''


'''
需要移除一些字母或数字，让最后结果最大或最小。
根据当前结果的末尾，跟当前字符比较，决定取舍。==> 单调栈
每个字母仅在答案中出现一次，所以要有计数。
同时，已经在 stack 中的字母也要快速判断在不在，要用 hash set.

no need to answer len
T: O(N)
S: O(N)


Runtime: 49 ms, faster than 64.07% of Python3 online submissions for Remove Duplicate Letters.
Memory Usage: 13.9 MB, less than 87.68% of Python3 online submissions for Remove Duplicate Letters.
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        cnt = Counter(s)
        seen = set()
        for ch in s:
            if ch in seen:
                cnt[ch] -= 1
                continue
            while stack and stack[-1] >= ch and cnt[stack[-1]] > 1:
                cnt[stack[-1]] -= 1
                seen.discard(stack[-1])
                stack.pop()
                
            stack.append(ch)
            seen.add(ch)
            
        return ''.join(stack)



