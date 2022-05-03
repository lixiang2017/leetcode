'''
DP
计算贡献
T: O(3N)
S: O(2N)

对每一个字符i，向前找到相同的字符j，向后找到相同的字符k。当前字符对最终结果的贡献是：（i-j）*(k-i)。
这相当于两种方案的拼接：在字符串A（j到i）当中，字符i贡献的次数是（i-j）次。
在字符串B(k-i)当中，字符i贡献的次数是（k-i）。那么当两者拼接的时候，字符i对子串（j到k）的贡献就是两种方案的乘积（符合乘法公式）。


最后答案数值估计：
更新：数据范围改成了 10^5 了。原来的范围是 10^4，答案不会超过 int。
这个题 “答案可能非常大” 是吓唬人的，
对于 10^4 长度的字符串，其字串数目 = n(n+1)/2 < 5.1*10^7，而每个子串的唯一字符个数最大为 26，总数为 26 * 5.1 * 10^7 = 1.3 * 10^9 < INT_MAX
因此只需要用 INT 来保存结果


执行用时：336 ms, 在所有 Python3 提交中击败了44.64% 的用户
内存消耗：23.2 MB, 在所有 Python3 提交中击败了5.36% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        left, right = [-1] * n, [n] * n
        pos = dict()
        for i, ch in enumerate(s):
            if ch in pos:
                left[i] = pos[ch]
            pos[ch] = i
            
        pos = dict()
        for i in range(n - 1, -1, -1):
            ch = s[i]
            if ch in pos:
                right[i] = pos[ch]
            pos[ch] = i 

        ans = 0
        for i in range(n):
            ans += (i - left[i]) * (right[i] - i)
        return ans 


'''
把乘法改成加法，每一次都计算贡献

执行用时：2168 ms, 在所有 Python3 提交中击败了16.07% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了88.69% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        ans = 0
        for ch in string.ascii_uppercase:
            l = r = -1
            for j in range(n):
                if s[j] == ch:
                    l, r = r, j 
                ans += r - l 
        return ans 


'''
执行用时：248 ms, 在所有 Python3 提交中击败了77.38% 的用户
内存消耗：19.8 MB, 在所有 Python3 提交中击败了41.07% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch].append(i)
        
        ans = 0
        for p in pos.values():
            p = [-1] + p + [n]
            for j in range(1, len(p) - 1):
                ans += (p[j] - p[j - 1]) * (p[j + 1] - p[j])
        return ans 
        

        

