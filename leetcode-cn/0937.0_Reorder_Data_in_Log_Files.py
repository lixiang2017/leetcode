'''
执行用时：40 ms, 在所有 Python3 提交中击败了48.98% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了61.18% 的用户
通过测试用例：65 / 65
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit = [], []
        for log in logs:
            identifier, content = log.split(maxsplit = 1)
            if '0' <= content[0] <= '9':
                digit.append(log)
            else:
                letter.append((content, identifier))
        letter.sort()
        return [identifier + ' ' + content for content, identifier in letter] + digit 


'''
执行用时：40 ms, 在所有 Python3 提交中击败了48.98% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了67.48% 的用户
通过测试用例：65 / 65
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit = [], []
        for log in logs:
            identifier, content = log.split(maxsplit = 1)
            if not content[0].isalpha():
                digit.append(log)
            else:
                letter.append((content, identifier))
        letter.sort()
        return [identifier + ' ' + content for content, identifier in letter] + digit 


'''
执行用时：40 ms, 在所有 Python3 提交中击败了48.98% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了96.14% 的用户
通过测试用例：65 / 65
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit = [], []
        for log in logs:
            identifier, content = log.split(maxsplit = 1)
            if content[0].isdigit():
                digit.append(log)
            else:
                letter.append((content, identifier))
        letter.sort()
        return [identifier + ' ' + content for content, identifier in letter] + digit 

      
'''
执行用时：40 ms, 在所有 Python3 提交中击败了48.98% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了82.11% 的用户
通过测试用例：65 / 65
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def compare(log):
            identifier, content = log.split(maxsplit = 1)
            if content[0].isdigit():
                return (1, )
            else:
                return (0, content, identifier)

        logs.sort(key = compare)
        return logs 


'''
执行用时：28 ms, 在所有 Python3 提交中击败了98.98% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了85.16% 的用户
通过测试用例：65 / 65
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def compare(log):
            identifier, content = log.split(' ', 1)
            return (1, ) if content[0].isdigit() else (0, content, identifier)

        logs.sort(key = compare)
        return logs 
           

