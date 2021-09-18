'''
Hash Table

You are here!
Your runtime beats 43.23 % of python3 submissions
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = Counter(nums1), Counter(nums2)
        ans = []
        for k, c in c1.items():
            ans.extend(min(c, c2[k]) * [k])
        return ans


'''
Follow up:

    What if the given array is already sorted? How would you optimize your algorithm?

You are here!
Your runtime beats 95.91 % of python3 submissions.
You are here!
Your memory usage beats 69.97 % of python3 submissions.
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort(), nums2.sort()
        M, N = len(nums1), len(nums2)
        i = j = 0
        ans = []
        while i < M and j < N:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans



'''
You are here!
Your runtime beats 95.91 % of python3 submissions.
You are here!
Your memory usage beats 89.69 % of python3 submissions.
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for k, c in (Counter(nums1) & Counter(nums2)).items():
            for _ in range(c):
                yield k



'''
one line
You are here!
Your runtime beats 70.55 % of python3 submissions.
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return reduce(lambda x, it: x + [it[0]] * it[1], (Counter(nums1) & Counter(nums2)).items(), [])










