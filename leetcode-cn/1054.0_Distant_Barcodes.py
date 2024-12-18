'''
heapq
T: O(NlogN)
S: O(N)

执行用时：168 ms, 在所有 Python3 提交中击败了20.00% 的用户
内存消耗：17.1 MB, 在所有 Python3 提交中击败了32.00% 的用户
通过测试用例：58 / 58
'''
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        h = [(-c, k) for k, c in cnt.items()]
        heapify(h)
        ans = []
        while h:
            if len(h) >= 2:
                neg_c1, k1 = heappop(h)
                neg_c2, k2 = heappop(h)
                ans.extend([k1, k2])
                if neg_c1 != -1:
                    heappush(h, (neg_c1 + 1, k1))
                if neg_c2 != -1:
                    heappush(h, (neg_c2 + 1, k2))
            else:
                neg_c, k = heappop(h)
                ans += [k] * (-neg_c)
                
        return ans 

'''
执行用时：76 ms, 在所有 Python3 提交中击败了92.25% 的用户
内存消耗：18.3 MB, 在所有 Python3 提交中击败了13.18% 的用户
通过测试用例：58 / 58
'''
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        data = []
        for v, c in Counter(barcodes).most_common():
            data += [v] * c
        ans = [0] * n
        ans[:: 2] = data[:(n + 1) // 2]
        ans[1:: 2] = data[(n + 1)// 2: ]
        return ans 
        