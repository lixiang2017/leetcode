'''
hash table

执行用时：36 ms, 在所有 Python3 提交中击败了99.05% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了17.14% 的用户
通过测试用例：52 / 52
'''
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = Counter()
        for cpdomain in cpdomains:
            rep, domain = cpdomain.split()
            rep = int(rep)
            parts = domain.split('.')
            for i, part in enumerate(parts):
                subdomain = '.'.join(parts[i: ])
                cnt[subdomain] += rep 
        return [str(c) + ' ' + subdomain for subdomain, c in cnt.items()]
