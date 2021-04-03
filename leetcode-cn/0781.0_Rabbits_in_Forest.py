'''
approach: Hash Table
Time: O(N + N) = O(N)
Space: O(N)

执行用时: 32 ms, 在所有 Python 提交中击败了19%的用户
内存消耗: 13.2 MB, 在所有 Python 提交中击败了44%的用户
'''


class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        from collections import Counter
        replies = Counter(answers)
        rabbits = 0
        for reply, cnt in replies.iteritems():
            if 0 == cnt % (reply + 1):
                rabbits += cnt
            else:
                rabbits += (cnt / (reply + 1) + 1) * (reply + 1)
        return rabbits

'''
approach: Hash Table
Time: O(N + N) = O(N)
Space: O(N)
执行用时：36 ms, 在所有 Python 提交中击败了12.50%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了6.25%的用户
'''

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        from collections import Counter
        from math import ceil

        replies = Counter(answers)
        rabbits = 0
        for reply, cnt in replies.iteritems():
            rabbits += int(ceil(1.0 * cnt / (reply + 1)) * (reply + 1))
        return rabbits


'''
approach: Hash Table
Time: O(N + N) = O(N)
Space: O(N)
执行用时：32 ms, 在所有 Python 提交中击败了18.75%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了68.75%的用户
'''
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        from collections import Counter
        from math import ceil

        replies = Counter(answers)
        rabbits = 0
        for reply, cnt in replies.iteritems():
            #rabbits += int(ceil(1.0 * cnt / (reply + 1)) * (reply + 1))
            rabbits += (cnt + reply) / (reply + 1) * (reply + 1)    # the same as above
        return rabbits



'''
approach: Hash Table with Only One Pass
Time: O(N)
Space: O(N)

执行用时：28 ms, 在所有 Python 提交中击败了75.00%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了31.25%的用户
'''

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        rabbits, cnt = 0, {}
        for answer in answers:
            if cnt.get(answer, 0):
                cnt[answer] -= 1
            else:
                cnt[answer] = answer
                rabbits += answer + 1
        return rabbits