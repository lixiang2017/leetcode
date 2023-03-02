'''
two pointers
T: O(N)
S: O(1)

Runtime: 68 ms, faster than 28.47% of Python3 online submissions for String Compression.
Memory Usage: 13.9 MB, less than 96.79% of Python3 online submissions for String Compression.
'''
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = j = 0
        while i < n:
            k = i + 1
            while k < n and chars[k] == chars[i]:
                k += 1
            cnt = k - i
            # store in the input character array
            if cnt == 1:
                chars[j] = chars[i]
                j += 1
            else:
                chars[j] = chars[i]
                j += 1
                q = deque(str(cnt))
                while q:
                    chars[j] = q.popleft()
                    j += 1
            # move to next group
            i = k
            
        return j

'''
two pointers
T: O(N)
S: O(1)

Runtime: 55 ms, faster than 92.53% of Python3 online submissions for String Compression.
Memory Usage: 13.9 MB, less than 96.79% of Python3 online submissions for String Compression.
'''
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = j = 0
        while i < n:
            k = i + 1
            while k < n and chars[k] == chars[i]:
                k += 1
            cnt = k - i
            # store in the input character array
            chars[j] = chars[i]
            j += 1
            if cnt > 1:
                q = deque(str(cnt))
                while q:
                    chars[j] = q.popleft()
                    j += 1
            # move to next group
            i = k
            
        return j

