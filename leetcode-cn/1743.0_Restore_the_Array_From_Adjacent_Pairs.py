'''
Hash Table + Hash Set,T:O(N),S:O(N)

执行用时：2128 ms, 在所有 Python3 提交中击败了5.26% 的用户
内存消耗：73.9 MB, 在所有 Python3 提交中击败了25.00% 的用户
'''
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pair = defaultdict(set)
        for a, b in adjacentPairs:
            pair[a].add(b)
            pair[b].add(a)

        x, y = adjacentPairs[0]
        ans = [x, y]
        added = set([x, y])

        while y in pair:
            Found = False
            for one in pair[y]:
                if one not in added:
                    Found = True
                    ans.append(one)
                    added.add(one)
                    y = one
            if not Found:
                break

        while x in pair:
            Found = False
            for one in pair[x]:
                if one not in added:
                    Found = True
                    ans.insert(0, one)
                    added.add(one)
                    x = one
            if not Found:
                break
        return ans
