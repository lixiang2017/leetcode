'''

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
