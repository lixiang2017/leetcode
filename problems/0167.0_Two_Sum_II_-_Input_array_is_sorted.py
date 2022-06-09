'''
Two Pointers
T: O(N)
S: O(1)

Runtime: 112 ms, faster than 16.87% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.6 MB, less than 86.50% of Python3 online submissions for Two Sum II - Input array is sorted.
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            t = numbers[l] + numbers[r]
            if t == target:
                return [l + 1, r + 1]
            elif t > target:
                r -= 1
            else:
                l += 1


'''
Hash Table
T: O(N)
S: O(N)

Runtime: 60 ms, faster than 89.52% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.7 MB, less than 32.95% of Python3 online submissions for Two Sum II - Input array is sorted.
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        book = {}
        for i, x in enumerate(numbers):
            if target - x in book:
                return [book[target - x], i + 1]
            book[x] = i + 1



'''
Binary Search
T: O(NlogN)
S: O(1)

Runtime: 128 ms, faster than 10.98% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.6 MB, less than 86.50% of Python3 online submissions for Two Sum II - Input array is sorted.
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, x in enumerate(numbers):
            l, r = i + 1, len(numbers) - 1
            while l <= r:
                mid = (l + r) >> 1
                if numbers[mid] == target - x:
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - x:
                    r = mid - 1
                else:
                    l = mid + 1
                

'''
Two Pointers
T: O(N)
S: O(1)

Runtime: 206 ms, faster than 34.32% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
Memory Usage: 15 MB, less than 41.52% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return [i + 1, j + 1]
        return []

