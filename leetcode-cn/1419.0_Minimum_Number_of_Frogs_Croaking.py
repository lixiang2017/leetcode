'''
hash table
T: O(5N)
S: O(1)

执行用时：240 ms, 在所有 Python3 提交中击败了25.58% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了8.84% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        index = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        cnt = [0] * 5
        ans = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                cnt[0] += 1
                ans = max(ans, sum(cnt))
            else:
                if cnt[index[ch] - 1] < 1:
                    return -1
                cnt[index[ch] - 1] -= 1
                cnt[index[ch]] += 1
                ans = max(ans, sum(cnt))
                if ch == 'k':
                    cnt[-1] = 0
        
        return -1 if sum(cnt) != 0 else ans 

'''
hash table
T: O(N)
S: O(1)

执行用时：192 ms, 在所有 Python3 提交中击败了40.93% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了8.84% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        index = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        cnt = [0] * 5
        ans = total = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                cnt[0] += 1
                total += 1
                ans = max(ans, total)
            else:
                if cnt[index[ch] - 1] < 1:
                    return -1
                cnt[index[ch] - 1] -= 1
                cnt[index[ch]] += 1
                ans = max(ans, total)
                if ch == 'k':
                    total -= cnt[-1]
                    cnt[-1] = 0
        
        return -1 if total != 0 else ans 


'''
hash table
T: O(N)
S: O(1)

执行用时：196 ms, 在所有 Python3 提交中击败了39.54% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了8.84% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        index = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        cnt = [0] * 5
        ans = total = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                cnt[0] += 1
                total += 1
                ans = max(ans, total)
            else:
                if cnt[index[ch] - 1] < 1:
                    return -1
                cnt[index[ch] - 1] -= 1
                cnt[index[ch]] += 1
                ans = max(ans, total)
                if ch == 'k':
                    total -= 1
        
        return -1 if total != 0 else ans 


'''
执行用时：184 ms, 在所有 Python3 提交中击败了44.65% 的用户
内存消耗：16.8 MB, 在所有 Python3 提交中击败了5.12% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs) % 5:
            return -1
        index = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        cnt = [0] * 5
        ans = total = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                cnt[0] += 1
                total += 1
                ans = max(ans, total)
            else:
                if cnt[index[ch] - 1] < 1:
                    return -1
                cnt[index[ch] - 1] -= 1
                cnt[index[ch]] += 1
                ans = max(ans, total)
                if ch == 'k':
                    total -= 1
        
        return -1 if total != 0 else ans 

