'''
rolling accumulation
T: O(N)
S: O(N)

执行用时：44 ms, 在所有 Python3 提交中击败了93.18% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了42.33% 的用户
通过测试用例：95 / 95
'''
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        cnt1 = distance = 0
        for i, ch in enumerate(boxes):
            if ch == '1':
                cnt1 += 1
                distance += i 
        ans = [distance]
        left1 = 0
        for i in range(1, len(boxes)):
            left1 += int(boxes[i - 1])
            distance += left1
            distance -= (cnt1 - left1)
            ans.append(distance)
        return ans 
