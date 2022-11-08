'''
执行用时：40 ms, 在所有 Python3 提交中击败了89.22% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：346 / 346
'''
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1: -1]
        ans = []

        def choices(part):
            if len(part) == 1:
                yield part 
            else:
                if part[0] != '0':
                    yield part 
                for i in range(len(part) - 1):
                    integer = part[: i + 1]
                    fraction = part[i + 1: ]
                    if (i > 0 and integer[0] == '0') or fraction[-1] == '0':
                        continue 
                    yield integer + '.' + fraction

        for i in range(len(s) - 1):
            former = s[: i + 1]
            latter = s[i + 1: ]
            for f1 in choices(former):
                for l1 in choices(latter):
                    ans.append(f'({f1}, {l1})')
        return ans 
        