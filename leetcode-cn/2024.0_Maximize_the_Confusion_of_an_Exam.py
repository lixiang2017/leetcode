'''
sliding window, while + while, T: O(N), S: O(1)

执行用时：588 ms, 在所有 Python3 提交中击败了8.69% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了42.61% 的用户
通过测试用例：93 / 93
'''
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        tally = Counter()
        n, left, right, ans = len(answerKey), 0, 0, 0
        while right < n:
            tally[answerKey[right]] += 1
            while min(tally['T'], tally['F']) > k:
                tally[answerKey[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans 


'''
sliding window, while + if, T: O(N), S: O(1)
使用if不会影响结果的正确性。始终保证最大窗口即可，没必要缩小窗口。

执行用时：588 ms, 在所有 Python3 提交中击败了8.69% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了67.83% 的用户
通过测试用例：93 / 93
'''
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        tally = Counter()
        n, left, right, ans = len(answerKey), 0, 0, 0
        while right < n:
            tally[answerKey[right]] += 1
            if min(tally['T'], tally['F']) > k:
                tally[answerKey[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans 

'''
省略掉ans变量. 最终结果即为最大窗口。right最终为n

执行用时：360 ms, 在所有 Python3 提交中击败了50.43% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了67.83% 的用户
通过测试用例：93 / 93
'''
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        tally = Counter()
        n, left, right = len(answerKey), 0, 0
        while right < n:
            tally[answerKey[right]] += 1
            if min(tally['T'], tally['F']) > k:
                tally[answerKey[left]] -= 1
                left += 1
            right += 1

        return right - left


'''
执行用时：380 ms, 在所有 Python3 提交中击败了45.22% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了66.96% 的用户
通过测试用例：93 / 93
'''
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        tally = Counter()
        n, left, right = len(answerKey), 0, 0
        for right in range(n):
            tally[answerKey[right]] += 1
            if min(tally['T'], tally['F']) > k:
                tally[answerKey[left]] -= 1
                left += 1

        return right - left + 1


