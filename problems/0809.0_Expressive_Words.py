'''
count 

执行用时：48 ms, 在所有 Python3 提交中击败了82.57% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了60.55% 的用户
通过测试用例：34 / 34
'''
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def count(w):
            chars = []
            cnt = []
            for ch in w:
                if not chars or chars[-1] != ch:
                    chars.append(ch)
                    cnt.append(1)
                else:
                    cnt[-1] += 1
            return chars, cnt 
        
        s_chars, s_cnt = count(s)

        def isStretchy(word):
            w_chars, w_cnt = count(word)
            if s_chars != w_chars or len(s_chars) != len(w_chars):
                return False
            for sc, wc in zip(s_cnt, w_cnt):
                if not (sc == wc or (sc > wc and sc >= 3)):
                    return False
            return True

        return sum(isStretchy(word) for word in words)
