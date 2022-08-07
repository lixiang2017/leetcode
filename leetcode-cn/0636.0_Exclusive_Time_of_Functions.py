'''
stack + simulation

执行用时：52 ms, 在所有 Python3 提交中击败了53.11% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了46.33% 的用户
通过测试用例：120 / 120
'''
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        for log in logs:
            parts = log.split(':')
            function_id, position, timestamp = int(parts[0]), parts[1], int(parts[2])
            if position == 'start':
                stack.append((function_id, timestamp))
            else:
                _, t = stack.pop()
                ans[function_id] += timestamp - t + 1
                if stack:
                    ans[stack[-1][0]] -= (timestamp - t + 1)
        return ans  

'''
输入：
8
["0:start:0","1:start:5","2:start:6","3:start:9","4:start:11","5:start:12","6:start:14","7:start:15","1:start:24","1:end:29","7:end:34","6:end:37","5:end:39","4:end:40","3:end:45","0:start:49","0:end:54","5:start:55","5:end:59","4:start:63","4:end:66","2:start:69","2:end:70","2:start:74","6:start:78","0:start:79","0:end:80","6:end:85","1:start:89","1:end:93","2:end:96","2:end:100","1:end:102","2:start:105","2:end:109","0:end:114"]
输出：
[110,3,92,7,6,9,12,20]
预期结果：
[20,14,35,7,6,9,10,14]
'''
