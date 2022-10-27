'''
hash table + hash set + sort

执行用时：44 ms, 在所有 Python3 提交中击败了40.55% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了40.13% 的用户
通过测试用例：16 / 16
'''
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        not_appear = []
        cnt = Counter(arr1)
        set2 = set(arr2)
        appear = []
        for x in arr2:
            if x in cnt:
                appear += [x] * cnt[x]
        for x in arr1:
            if x not in set2:
                not_appear.append(x)
        return appear + sorted(not_appear)


'''
执行用时：52 ms, 在所有 Python3 提交中击败了16.07% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了56.72% 的用户
通过测试用例：16 / 16
'''
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort(key=lambda x: arr2.index(x) if x in arr2 else x + len(arr2))
        return arr1
        
