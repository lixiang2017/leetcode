'''
mask(binary enumeration) + binary search
T: O((2^m)^2)) + O((2^m)^2) * log((2^m)^2)) + O(N * log((2^m)^2))

执行用时：288 ms, 在所有 Python3 提交中击败了68.84% 的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了31.16% 的用户
通过测试用例：89 / 89
'''
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        n, m = len(baseCosts), len(toppingCosts)

        def toppingOneChoice():
            cand = set()
            for mask in range(1 << m):
                cost = sum(toppingCosts[i] for i in range(m) if (mask >> i) & 1)
                cand.add(cost)
            return list(cand)
        
        oneTopping = toppingOneChoice()
        twoTopping = list(set(sum(p) for p in combinations_with_replacement(oneTopping, 2)))
        twoTopping.sort()

        ans = baseCosts[0]
        for base in baseCosts:
            remain = target - base
            idx = bisect_left(twoTopping, remain)
            for i in [idx - 1, idx]:
                if 0 <= i < len(twoTopping):
                    t = base + twoTopping[i]
                    if abs(t - target) < abs(ans - target) or (abs(t - target) == abs(ans - target) and t < ans):
                        ans = t
                        if ans == target:
                            return target
        return ans 


'''
product(oneTopping, repeat=2)

执行用时：572 ms, 在所有 Python3 提交中击败了42.75% 的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了30.44% 的用户
通过测试用例：89 / 89
'''
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        n, m = len(baseCosts), len(toppingCosts)

        def toppingOneChoice():
            cand = set()
            for mask in range(1 << m):
                cost = sum(toppingCosts[i] for i in range(m) if (mask >> i) & 1)
                cand.add(cost)
            return list(cand)
        
        oneTopping = toppingOneChoice()
        twoTopping = list(set(sum(p) for p in product(oneTopping, repeat=2)))
        twoTopping.sort()

        ans = baseCosts[0]
        for base in baseCosts:
            remain = target - base
            idx = bisect_left(twoTopping, remain)
            for i in [idx - 1, idx]:
                if 0 <= i < len(twoTopping):
                    t = base + twoTopping[i]
                    if abs(t - target) < abs(ans - target) or (abs(t - target) == abs(ans - target) and t < ans):
                        ans = t
                        if ans == target:
                            return target
        return ans 


