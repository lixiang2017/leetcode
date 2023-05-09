'''
T: O(1)
S: O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了27.92% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了8.44% 的用户
通过测试用例：53 / 53
'''
class Solution:
    def countTime(self, time: str) -> int:
        h, m = time.split(':')
        ans = 1
        if h == '??':
            ans = 24
        elif h[0] == '?':
            if h[1] <= '3':
                ans = 3
            else:
                ans = 2
        elif h[1] == '?':
            if h[0] == '2':
                ans = 4
            else:
                ans = 10
        
        if m == '??':
            ans *= 60
        elif m[0] == '?':
            ans *= 6
        elif m[1] == '?':
            ans *= 10

        return ans 

'''
T: O(24 + 60)
S: O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了27.92% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了7.79% 的用户
通过测试用例：53 / 53
'''
class Solution:
    def countTime(self, time: str) -> int:
        h, m = time.split(':')

        def match_hour_cnt(h):
            cnt = 0
            for i in range(24):
                i = str(i).zfill(2)
                if all(ch1 == ch2 for ch1, ch2 in zip(i, h) if ch2 != '?'):
                    cnt += 1
            return cnt 
        
        def match_minute_cnt(m):
            cnt = 0
            for i in range(60):
                i = str(i).zfill(2)
                if all(ch1 == ch2 for ch1, ch2 in zip(i, m) if ch2 != '?'):
                    cnt += 1
            return cnt 
        
        return match_hour_cnt(h) * match_minute_cnt(m)


'''
T: O(24 + 60)
S: O(1)

执行用时：60 ms, 在所有 Python3 提交中击败了11.04% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了7.79% 的用户
通过测试用例：53 / 53
'''
class Solution:
    def countTime(self, time: str) -> int:
        def match_cnt(part, upper):
            cnt = 0
            for i in range(upper):
                i = str(i).zfill(2)
                if all(ch1 == ch2 for ch1, ch2 in zip(i, part) if ch2 != '?'):
                    cnt += 1
            return cnt 
        
        h, m = time.split(':')
        return match_cnt(h, 24) * match_cnt(m, 60)

'''
T: O(24 + 60)
S: O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了16.23% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了8.44% 的用户
通过测试用例：53 / 53
'''
class Solution:
    def countTime(self, time: str) -> int:
        def match_cnt(part, upper):
            return sum(1 if all(ch1 == ch2 for ch1, ch2 in zip(str(i).zfill(2), part) if ch2 != '?') else 0 for i in range(upper))

        h, m = time.split(':')
        return match_cnt(h, 24) * match_cnt(m, 60)

'''
T: O(24 + 60)
S: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了68.83% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了5.19% 的用户
通过测试用例：53 / 53
'''
class Solution:
    def countTime(self, time: str) -> int:
        def match_cnt(part, upper):
            return sum(1 if all(ch1 == ch2 for ch1, ch2 in zip(str(i).zfill(2), part) if ch2 != '?') else 0 for i in range(upper))

        return match_cnt(time[: 2], 24) * match_cnt(time[3: ], 60)

'''
T: O(24 + 60)
S: O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了27.92% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了5.19% 的用户
通过测试用例：53 / 53
'''
class Solution:
    def countTime(self, time: str) -> int:
        def match_cnt(part, upper):
            return sum(all(ch1 == ch2 or ch2 == '?' for ch1, ch2 in zip(str(i).zfill(2), part)) for i in range(upper))

        return match_cnt(time[: 2], 24) * match_cnt(time[3: ], 60)


'''
T: O(24 * 60)
S: O(1)

执行用时：144 ms, 在所有 Python3 提交中击败了5.19% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了7.14% 的用户
通过测试用例：53 / 53
'''
class Solution:
    def countTime(self, time: str) -> int:
        def match(compose):
            return all(ch1 == ch2 or ch2 == '?' for ch1, ch2 in zip(compose, time))

        return sum(match(f'{h:02d}:{m:02d}') for h in range(24) for m in range(60))
