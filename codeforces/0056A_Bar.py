'''
#   When    Who Problem Lang    Verdict Time    Memory
162651259   Jul/03/2022 22:06UTC+8  lixiang2022 56A - Bar   PyPy 3-64   Accepted    218 ms  500 KB

'''

n = int(input())
ans = 0
alcohol = {"ABSINTH", "BEER",
    "BRANDY", "CHAMPAGNE",
    "GIN", "RUM", "SAKE", 
    "TEQUILA", "VODKA", 
    "WHISKEY", "WINE"}

for _ in range(n):
    line = input()
    if line.isdigit():
        if int(line) < 18:
            ans += 1
    else:
        if line in alcohol:
            ans += 1
print(ans)
