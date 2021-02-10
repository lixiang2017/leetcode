'''
Time: O(N)
Space: O(N)

执行结果：通过
显示详情
执行用时：
12 ms, 在所有 Python 提交中击败了97.28%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.44%的用户
'''

class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        number = number.replace(' ', '').replace('-', '')
        size = len(number)
        group = ''

        while size > 4:
            group += number[: 3]
            group += '-'
            size -= 3
            number = number[3:]
        
        if 4 == size:
            group += number[:2] + '-' + number[2:]
        elif 3 == size or 2 == size:
            group += number

        return group


'''
执行结果：
通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了83.67%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了25.17%的用户
'''

class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        num = number.replace(' ', '').replace('-', '')
        parts = []
        for i in range(0, len(num), 3):
            parts.append(num[i: i + 3])
        
        if len(parts) >= 2 and  1 == len(parts[-1]):
            parts[-1] = parts[-2][-1] + parts[-1]
            parts[-2] = parts[-2][:2]

        return '-'.join(parts)



'''
approach: Two Pointers
Time: O(N)
Space: O(N)

执行结果：
通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了27.89%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了78.23%的用户
'''

class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        num = number.replace(' ', '').replace('-', '')
        parts = []

        left, right = 0, len(num)
        while right - left > 4:
            parts.append(num[left: left + 3])
            left += 3

        if right - left == 4:
            parts.append(num[left: left + 2])
            parts.append(num[left + 2 : ])
        else:
            parts.append(num[left: ])    

        return '-'.join(parts)




