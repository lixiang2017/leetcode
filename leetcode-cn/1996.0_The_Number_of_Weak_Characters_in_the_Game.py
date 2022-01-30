'''
sort + increasing stack

执行用时：600 ms, 在所有 Python3 提交中击败了28.57% 的用户
内存消耗：49.5 MB, 在所有 Python3 提交中击败了12.93% 的用户
通过测试用例：44 / 44

# sort
[[3,6],[5,5],[6,3]]
[[2,2],[3,3]]
[[1,5],[4,3],[10,4]]
'''

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda p: (p[0], -p[1]))
        n = len(properties)
        max_attack = 0
        # increase defense stack
        defense_stack = []
        ans = 0
        for i in range(n - 1, -1, -1):
            attack, defense = properties[i]
            if attack < max_attack and defense_stack and defense_stack[-1] > defense:
                ans += 1
            max_attack = max(max_attack, attack)
            if not defense_stack or defense_stack[-1] < defense:
                defense_stack.append(defense)

        return ans

