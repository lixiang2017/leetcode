'''
hash table + sort

执行用时：208 ms, 在所有 Python3 提交中击败了63.46% 的用户
内存消耗：36.4 MB, 在所有 Python3 提交中击败了37.50% 的用户
通过测试用例：77 / 77
'''
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        name2times = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            h, m = time.split(':')
            t = int(h) * 60 + int(m)
            name2times[name].append(t)
        
        def isAlert(times):
            n = len(times)
            for i in range(2, n):
                t1, t2 = times[i - 2], times[i]
                if t2 - t1 <= 60:
                    return True
            return False

        ans = []
        for name, times in name2times.items():
            times.sort()
            if isAlert(times):
                ans.append(name)

        return sorted(ans)
