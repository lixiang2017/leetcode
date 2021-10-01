'''
Hash Table + Sort
Time: O(N + NlogN)
Space: O(N)

'''
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        c = Counter(arr)
        nums = sorted(c.keys())
        for n in nums:
            if n in c:
                if n < 0:
                    if (n % 2) or (n / 2) not in c or c[n/2] < c[n]:
                        return False                    
                    if c[n/2] == c[n]:
                        c.pop(n/2)
                    else:
                        c[n/2] -= c[n]
                    c.pop(n)
                elif 0 == n:
                    if c[n] % 2:
                        return False
                    c.pop(0)
                else:
                    if n * 2 not in c or c[n * 2] < c[n]:
                        return False
                    if c[n * 2] == c[n]:
                        c.pop(n * 2)
                    else:
                        c[n * 2] -= c[n]
                    c.pop(n)
                    
        return True


'''
Hash Table + Sort
Time: O(N + NlogN)
Space: O(N)

You are here!
Your runtime beats 78.67 % of python3 submissions.
You are here!
Your memory usage beats 30.33 % of python3 submissions.
'''
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        c = Counter(arr)
        nums = sorted(c.keys(), key=abs)
        for n in nums:
            if c[n * 2] < c[n]:
                return False
            c[n * 2] -= c[n]
                    
        return True

'''
Hash Table + Sort
Time: O(N + NlogN)
Space: O(N)

You are here!
Your runtime beats 88.15 % of python3 submissions.
You are here!
Your memory usage beats 78.20 % of python3 submissions.
'''
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        c = Counter(arr)
        for n in sorted(c, key=abs):
            if c[n * 2] < c[n]:
                return False
            c[n * 2] -= c[n]
                    
        return True





