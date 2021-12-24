'''
Binary Search + Rabin Karp(Rolling Hash) * 2
T: O(NlogN), S: O(N)

执行用时：2156 ms, 在所有 Python3 提交中击败了55.24% 的用户
内存消耗：21.7 MB, 在所有 Python3 提交中击败了41.43% 的用户
通过测试用例：67 / 67
'''
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        arr = [ord(ch) - ord('a') for ch in s]
        # base
        b1, b2 = random.randint(26, 100), random.randint(26, 100)
        # mod
        m1, m2 = random.randint(10**9 + 7, 1 << 32), random.randint(10**9 + 7, 1 << 32)
        n = len(s)
        l, r = 1, n - 1
        start, _len = -1, 0
        while l <= r:
            mid = (l + r) // 2
            idx = self.check(arr, n, mid, b1, b2, m1, m2)
            if idx != -1:
                l = mid + 1
                start = idx 
                _len = mid 
            else:
                r = mid - 1

        return s[start: start + _len] if start != -1 else ''
    
    def check(self, arr, n, mid, b1, b2, m1, m2):
        # Rabin-Karp, rolling hash
        h1, h2 = 0, 0
        for i in range(mid):  # 0...(mid - 1)
            h1 = (h1 * b1 + arr[i]) % m1 
            h2 = (h2 * b2 + arr[i]) % m2 
        p1 = pow(b1, mid, m1)
        p2 = pow(b2, mid, m2)
        # seen pair (h1, h2)
        seen = {(h1, h2)}
        for i in range(mid, n):
            h1 = (h1 * b1 - arr[i - mid] * p1 + arr[i]) % m1 
            h2 = (h2 * b2 - arr[i - mid] * p2 + arr[i]) % m2 
            if (h1, h2) in seen:
                # i-mid+1 ... i
                return i - mid + 1
            seen.add((h1, h2))

        return -1


'''
执行用时：3456 ms, 在所有 Python3 提交中击败了25.71% 的用户
内存消耗：232.1 MB, 在所有 Python3 提交中击败了9.05% 的用户
通过测试用例：67 / 67
'''
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        global n, ans
        n, ans = len(s), ''
        l, r = 0, n
        while l < r:
            mid = (l + r + 1) // 2
            if self.check(s, mid):
                l = mid 
            else:
                r = mid - 1
        return ans 

    def check(self, s: str, mid: int) -> bool:
        visited = set()
        for i in range(n - mid + 1): # 0 1 2 3 4 5 n = 6, mid = 2, i can be 4
            cur = s[i: i + mid]
            if cur in visited:
                global ans 
                ans = cur 
                return True 
            else:
                visited.add(cur)
        return False 
        