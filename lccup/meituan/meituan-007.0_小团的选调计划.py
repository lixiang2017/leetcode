'''
执行用时：28 ms, 在所有 Python3 提交中击败了50.00% 的用户
内存消耗：10 MB, 在所有 Python3 提交中击败了8.33% 的用户
'''
n = int(input())
want = []
for _ in range(n):
    want.append(list(map(int, input().split())))

distr = []
occupied = [False] * n
for i in range(n):
    for w in want[i]:
        if not occupied[w - 1]:
            distr.append(w)
            occupied[w - 1] = True
            break

print(' '.join(map(str, distr)))

'''
输入：
5
1 5 3 4 2 
2 3 5 4 1 
5 4 1 2 3 
1 2 5 4 3 
1 4 5 2 3
输出：1 2 5 4 3


5
5 4 1 2 3 
1 2 5 4 3
1 5 3 4 2 
2 3 5 4 1  
1 4 5 2 3
'''


'''
执行用时：16 ms, 在所有 Python3 提交中击败了91.67% 的用户
内存消耗：9 MB, 在所有 Python3 提交中击败了50.00% 的用户
'''
n = int(input())
seen = set()
ans = []
for _ in range(n):
    for j in input().split():
        if j not in seen:
            ans.append(j)
            seen.add(j)
            break
print(' '.join(ans))
