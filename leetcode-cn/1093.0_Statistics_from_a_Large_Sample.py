'''
执行用时：48 ms, 在所有 Python3 提交中击败了23.53% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了5.88% 的用户
通过测试用例：52 / 52
'''
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum, maximum, total, total_cnt, mode = 255, 0, 0, 0, 0
        for i, cnt in enumerate(count):
            if cnt > 0:
                if i < minimum:
                    minimum = i 
                if i > maximum:
                    maximum = i 
                total += i * cnt 
                total_cnt += cnt 
                if cnt > count[mode]:
                    mode = i 
        mean = total / total_cnt

        pairs = [(i, cnt) for i, cnt in enumerate(count) if cnt != 0]
        n = len(pairs)
        l, r = 0, n - 1
        cnt_l = cnt_r = 0
        while l <= r:
            if cnt_l < cnt_r:
                cnt_l += pairs[l][1]
                l += 1
            else:
                cnt_r += pairs[r][1]
                r -= 1
        l -= 1
        r += 1
        if cnt_l == cnt_r:
            median = (pairs[l][0] + pairs[r][0]) / 2
        elif cnt_l > cnt_r:
            median = pairs[l][0]
        else:
            median = pairs[r][0]           
        return [minimum, maximum, mean, median, mode]
        