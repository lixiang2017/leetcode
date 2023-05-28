'''
merge sort

执行用时：80 ms, 在所有 Python3 提交中击败了88.89% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了62.96% 的用户
通过测试用例：72 / 72
'''
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def merge(f: List[int], g: List[int], k: int) -> List[int]:
            if len(g) > len(f):
                return merge(g, f, k)
            # (_sum, index for f, index for g)
            q = [(f[0] + g[i], 0, i) for i in range(len(g))]
            heapify(q)
            taken = []
            while k and q:
                entry = heappop(q)
                taken.append(entry[0])
                if entry[1] + 1 < len(f):
                    heappush(q, (f[entry[1] + 1] + g[entry[2]] , entry[1] + 1, entry[2]))
                k -= 1
            return taken 

        prev = mat[0]
        for i in range(1, len(mat)):
            prev = merge(prev, mat[i], k)
        return prev[k - 1]


'''
执行用时：72 ms, 在所有 Python3 提交中击败了98.77% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了62.96% 的用户
通过测试用例：72 / 72
'''
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def merge(f: List[int], g: List[int], k: int) -> List[int]:
            if len(g) > len(f):
                return merge(g, f, k)
            # (_sum, index for f, index for g)
            q = [(f[0] + g[i], 0, i) for i in range(len(g))]
            heapify(q)
            taken = []
            while k and q:
                _sum, idx_f, idx_g = heappop(q)
                taken.append(_sum)
                if idx_f + 1 < len(f):
                    heappush(q, (f[idx_f + 1] + g[idx_g] , idx_f + 1, idx_g))
                k -= 1
            return taken 

        prev = mat[0]
        for i in range(1, len(mat)):
            prev = merge(prev, mat[i], k)
        return prev[k - 1]

'''
执行用时：136 ms, 在所有 Python3 提交中击败了23.46% 的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了49.38% 的用户
通过测试用例：72 / 72
'''
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def merge(f: List[int], g: List[int], k: int) -> List[int]:
            left, right, threshold = f[0] + g[0], f[-1] + g[-1], 0
            k = min(k, len(f) * len(g))
            while left <= right:
                mid = (left + right) // 2
                rptr, cnt = len(g) - 1, 0
                for lptr, x in enumerate(f):
                    while rptr >= 0 and x + g[rptr] > mid:
                        rptr -= 1
                    cnt += rptr + 1
                if cnt >= k:
                    threshold = mid
                    right = mid - 1
                else:
                    left = mid + 1 

            taken = []
            for i, x in enumerate(f):
                for j, y in enumerate(g):
                    if (total := x + y) < threshold:
                        taken.append(total)
                    else:
                        break

            taken += [threshold] * (k - len(taken))
            taken.sort()
            return taken 

        prev = mat[0]
        for i in range(1, len(mat)):
            prev = merge(prev, mat[i], k)
        return prev[k - 1]



