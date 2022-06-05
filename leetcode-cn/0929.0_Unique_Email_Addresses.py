'''
执行用时：44 ms, 在所有 Python3 提交中击败了68.50% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了65.50% 的用户
通过测试用例：185 / 185
'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            unique.add(local + '@' + domain)
        return len(unique)

'''
执行用时：36 ms, 在所有 Python3 提交中击败了95.25% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了65.50% 的用户
通过测试用例：185 / 185
'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+', 1)[0].replace('.', '')
            unique.add(local + '@' + domain)
        return len(unique)


'''
执行用时：40 ms, 在所有 Python3 提交中击败了85.50% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了99.00% 的用户
通过测试用例：185 / 185
'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        process = lambda x: x.split('@')[0].split('+', 1)[0].replace('.', '') + '@' + x.split('@')[1]
        return len(set(process(email) for email in emails))


'''
one line
写法：
(lambda function)(arguments)

执行用时：44 ms, 在所有 Python3 提交中击败了68.50% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了64.00% 的用户
通过测试用例：185 / 185
'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        return len(set((lambda x: x.split('@')[0].split('+', 1)[0].replace('.', '') + '@' + x.split('@')[1])(email) for email in emails))


