'''
AC
'''

def printThisNumber(n):
    nums = {
        '0': 'ling',
        '1': 'yi',
        '2': 'er',
        '3': 'san',
        '4': 'si',
        '5': 'wu',
        '6': 'liu',
        '7': 'qi',
        '8': 'ba',
        '9': 'jiu'
    }
    
    s = sum([int(c) for c in str(n)])
    return ' '.join([nums[ch] for ch in str(s)])

n = input()
print printThisNumber(n)
