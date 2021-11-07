'''
41 / 51 个通过测试用例
状态：超出时间限制
brute force

T: O(N^2)
S: O(N)
'''
class Solution:
    def countVowels(self, word: str) -> int:
        N = len(word)
        pre = [0] * (N + 1)
        for i, ch in enumerate(word):
            if ch in 'aeiou':
                pre[i + 1] = pre[i] + 1
            else:
                pre[i + 1] = pre[i]

        ans = 0    
        for i in range(1, len(word) + 1):
            for j in range(i):
                ans += pre[i] - pre[j]

        return ans        

'''
   "aba"
   0112

'''


'''
前缀和+前缀和
这是从双层暴力优化过来的

通过
	296 ms	23.8 MB	Python3	2021/11/07 19:48	

T: O(3N)
S: O(2N)

ref:
https://leetcode-cn.com/problems/vowels-of-all-substrings/solution/cqian-zhui-he-qian-zhui-he-by-answerer-360n/
'''
class Solution:
    def countVowels(self, word: str) -> int:
        N = len(word)
        pre = [0] * (N + 1)
        for i, ch in enumerate(word):
            if ch in 'aeiou':
                pre[i + 1] = pre[i] + 1
            else:
                pre[i + 1] = pre[i]
                
        # presum of presum
        prepre = [0] * (N + 1)
        for i in range(1, N + 1):
            prepre[i] = prepre[i - 1] + pre[i]
            
        ans = 0
        for i in range(N):
            ans += pre[i + 1] * (i + 1) - prepre[i]
        return ans        
        

'''
乘法原理
T: O(N)
S: O(1)

执行用时：92 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def countVowels(self, word: str) -> int:
        ans, N = 0, len(word)
        for i, ch in enumerate(word):
            if ch in 'aeiou':
                ans += (i + 1) * (N - i)
        return ans        

