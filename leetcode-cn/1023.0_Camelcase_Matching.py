'''
two pointers

执行用时：32 ms, 在所有 Python3 提交中击败了88.24% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了32.94% 的用户
通过测试用例：36 / 36
'''
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        def match(q: str) -> bool:
            it = iter(q)
            for ch in pattern:
                while (nxt := next(it, None)) != ch:
                    if nxt is None or nxt.isupper():
                        return False
            for left in it:
                if left.isupper():
                    return False
            return True
        
        return [match(q) for q in queries]
