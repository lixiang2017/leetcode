'''
hashset + 排序 + 离散化 + 差分 + 二分

执行用时：204 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：37.1 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：52 / 52
'''
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        # time set
        times = set()
        for start, end in flowers:
            times.add(start)
            times.add(end + 1)
        times = sorted(times)
        n = len(times)
        diff = [0] * (n + 1)
        time2idx = {t: i for i, t in enumerate(times)}
        for start, end in flowers:
            idx_s = time2idx[start]
            diff[idx_s] += 1
            idx_e = time2idx[end + 1]
            diff[idx_e] -= 1
        
        ans = []
        cnt = list(accumulate(diff))
        for p in persons:
            idx = bisect_left(times, p)
            if idx == n or p != times[idx]:
                idx -=1
            ans.append(cnt[idx])
        return ans 

