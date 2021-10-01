'''
110 / 118 test cases passed.
	Status: Time Limit Exceeded
	
Submitted: 0 minutes ago
'''
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        N = len(arr)
        c = Counter(arr)
        if c[1] % 3 != 0:
            return [-1, -1]
        part = c[1] // 3
        # all zeros
        if 0 == part:
            return [0, 2]
        # [a1, a2)   [b1, b2)
        a1 = a2 = b1 = b2 = 0
        ones = i = 0
        while i < N and ones < part:
            if arr[i] == 1:
                ones += 1
            i += 1
        a1 = i - 1
        while i < N and ones < part + 1:
            if arr[i] == 1:
                ones += 1
            i += 1
        a2 = i - 1
        while i < N and ones < part * 2:
            if arr[i] == 1:
                ones += 1
            i += 1
        b1 = i - 1
        while i < N and ones < part * 2 + 1:
            if arr[i] == 1:
                ones += 1
            i += 1
        b2 = i - 1
        # cut
        for delta in range(min(a2 - a1, b2 - b1) + 1):
            first = ''.join(str(n) for n in arr[ : a1 + delta + 1]).lstrip('0')
            second = ''.join(str(n) for n in arr[a1 + delta + 1: b1 + delta + 1]).lstrip('0')
            third = ''.join(str(n) for n in arr[b1 + delta + 1: ]).lstrip('0')
            if first == second == third:
                return [a1 + delta, b1 + delta + 1]
        
        return [-1, -1]
        

'''
118 / 118 test cases passed.
	Status: Accepted
Runtime: 5988 ms
Memory Usage: 15.5 MB
	
You are here!
Your memory usage beats 23.16 % of python3 submissions.
'''
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        N = len(arr)
        c = Counter(arr)
        if c[1] % 3 != 0:
            return [-1, -1]
        part = c[1] // 3
        # all zeros
        if 0 == part:
            return [0, 2]
        # [a1, a2)   [b1, b2)
        a1 = a2 = b1 = b2 = 0
        ones = i = 0
        while i < N and ones < part:
            if arr[i] == 1:
                ones += 1
            i += 1
        a1 = i - 1
        while i < N and ones < part + 1:
            if arr[i] == 1:
                ones += 1
            i += 1
        a2 = i - 1
        while i < N and ones < part * 2:
            if arr[i] == 1:
                ones += 1
            i += 1
        b1 = i - 1
        while i < N and ones < part * 2 + 1:
            if arr[i] == 1:
                ones += 1
            i += 1
        b2 = i - 1
        # cut
        for delta in range(min(a2 - a1, b2 - b1) + 1):
            #first = ''.join(str(n) for n in arr[ : a1 + delta + 1]).lstrip('0')
            #second = ''.join(str(n) for n in arr[a1 + delta + 1: b1 + delta + 1]).lstrip('0')
            #third = ''.join(str(n) for n in arr[b1 + delta + 1: ]).lstrip('0')
            max_len = max(a1 + delta + 1, b1 - a1, N - (b1 + delta + 1))
            first = [0] * (max_len - (a1 + delta + 1)) + arr[ : a1 + delta + 1]
            second = [0] * (max_len - (b1 - a1)) + arr[a1 + delta + 1 : b1 + delta + 1]
            third = [0] * (max_len -(N - (b1 + delta + 1))) +  arr[b1 + delta + 1: ]
            if first == second == third:
                return [a1 + delta, b1 + delta + 1]
        
        return [-1, -1]
        
        
