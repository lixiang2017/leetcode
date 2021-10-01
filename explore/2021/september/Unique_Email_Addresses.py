'''
Hash Set

You are here!
Your runtime beats 87.08 % of python3 submissions.
You are here!
Your memory usage beats 59.86 % of python3 submissions.
'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for e in emails:
            local, domain = e.split('@')
            local = local.split('+')[0].replace('.', '')
            seen.add(local + '@' + domain)
        return len(seen)
