'''
approach: Mono Stack
Time: O(N)
Space: O(N)

执行用时：472 ms, 在所有 Python 提交中击败了38.46%的用户
内存消耗：17.4 MB, 在所有 Python 提交中击败了30.16%的用户
'''

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        N = len(T)
        days = [0] * N
        stack = []
        for i in range(N):
            while stack and T[i] > T[stack[-1]]:   
                idx = stack.pop()
                days[idx] = i - idx
            stack.append(i)

        return days


'''
monotonic stack
Time: O(N)
Space: O(N)

执行用时：196 ms, 在所有 Python3 提交中击败了57.50% 的用户
内存消耗：20.8 MB, 在所有 Python3 提交中击败了26.12% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        wait = [0] * N
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                pre = stack.pop()
                wait[pre] = i - pre
            stack.append(i)
        return wait 


'''
binary search

执行用时：7308 ms, 在所有 Python3 提交中击败了5.00% 的用户
内存消耗：23.1 MB, 在所有 Python3 提交中击败了7.07% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        MAX_VAL = n + 5
        ans = [0] * n
        t2indice = defaultdict(list)
        for i, t in enumerate(temperatures):
            t2indice[t].append(i)

        for i, t in enumerate(temperatures):
            m = MAX_VAL
            for ht in range(t + 1, 101):
                if ht in t2indice:
                    idx = bisect_right(t2indice[ht], i)
                    if idx < len(t2indice[ht]):
                        m = min(m, t2indice[ht][idx])
            if m < MAX_VAL:
                ans[i] = m - i 
        return ans


'''
跳跃性比较

 * 根据题意，从最后一天推到第一天，这样会简单很多。因为最后一天显然不会再有升高的可能，结果直接为0。
 * 再看倒数第二天的温度，如果比倒数第一天低，那么答案显然为1，如果比倒数第一天高，又因为倒数第一天
 * 对应的结果为0，即表示之后不会再升高，所以倒数第二天的结果也应该为0。
 * 自此我们容易观察出规律，要求出第i天对应的结果，只需要知道第i+1天对应的结果就可以：
 * - 若T[i] < T[i+1]，那么res[i]=1；
 * - 若T[i] > T[i+1]
 *   - res[i+1]=0，那么res[i]=0;
 *   - res[i+1]!=0，那就比较T[i]和T[i+1+res[i+1]]（即将第i天的温度与比第i+1天大的那天的温度进行比较）


执行用时：196 ms, 在所有 Python3 提交中击败了74.02% 的用户
内存消耗：21 MB, 在所有 Python3 提交中击败了98.35% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n:
                if temperatures[i] < temperatures[j]:
                    ans[i] = j - i 
                    break 
                else:
                    if ans[j] != 0:
                        j += ans[j]
                    else:
                        break
        return ans



'''
跳跃性比较

执行用时：184 ms, 在所有 Python3 提交中击败了89.06% 的用户
内存消耗：21 MB, 在所有 Python3 提交中击败了98.19% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n:
                if temperatures[i] < temperatures[j]:
                    ans[i] = j - i 
                    break 
                elif ans[j] != 0:
                        j += ans[j]
                else:
                    break
        return ans


'''
跳跃性比较, int a recursive way

执行用时：244 ms, 在所有 Python3 提交中击败了33.28% 的用户
内存消耗：30.4 MB, 在所有 Python3 提交中击败了5.03% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n

        def getHigherDelta(i: int, j: int):
            if temperatures[i] < temperatures[j]:
                return j - i
            elif ans[j] == 0:
                return 0
            else:
                return getHigherDelta(i, j + ans[j])

        for i in range(n - 2, -1, -1):
            ans[i] = getHigherDelta(i, i + 1)
        return ans


'''
倒序遍历, 记录温度与下标关系
T: O(MN) = O(100 * N)
S: O(M)

执行用时：3312 ms, 在所有 Python3 提交中击败了5.00% 的用户
内存消耗：21.1 MB, 在所有 Python3 提交中击败了95.52% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        MAX_VAL = n + 5
        # for every temperature, next index 
        next_index = [MAX_VAL] * 101
        ans = [0] * n

        for i in range(n - 1, -1, -1):
            idx = MAX_VAL
            for t in range(temperatures[i] + 1, 101):
                idx = min(idx, next_index[t])
            if idx < MAX_VAL:
                ans[i] = idx - i 
            next_index[temperatures[i]] = i 
        return ans


'''
倒序遍历+单调栈
与正序遍历+单调栈一直，栈中元素 栈底元素最大、栈顶元素最小。从栈底到栈顶降序。非增序
Time: O(N)
Space: O(N)

执行用时：256 ms, 在所有 Python3 提交中击败了26.80% 的用户
内存消耗：22.2 MB, 在所有 Python3 提交中击败了21.57% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        MAX_VAL = n + 5
        # for every temperature, next index 
        next_index = [MAX_VAL] * 101
        ans = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1][0] - i 
            stack.append((i, temperatures[i]))        
                
        return ans










