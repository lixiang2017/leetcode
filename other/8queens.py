'''
approach: backtracking

'''


choices = 0
# N = 1
# N = 4
N = 30
# board = [[0 for _ in range(N)] for _ in range(N)]
board = [0 for _ in range(N)]




def isValid(row):
    for j in range(row):
        if board[row] == board[j] or row - j == board[row] - board[j] or row - j == board[j] - board[row]:
            return False

    return True


def backtracking(row = 0):
    global N
    if row == N:
        # print choices
        global choices
        choices += 1
        return

    for col in range(N):
        board[row] = col
        if isValid(row):
            backtracking(row + 1)
        # board[row] = 0  # no need

# driver 
def main():
    for n in range(1, 15):
        global N, choices
        N = n
        choices = 0
        backtracking()
        print 'N: ', N, ', choices: ', choices

main()


'''
result
N:  1 , choices:  1
N:  2 , choices:  0
N:  3 , choices:  0
N:  4 , choices:  2
N:  5 , choices:  10
N:  6 , choices:  4
N:  7 , choices:  40
N:  8 , choices:  92
N:  9 , choices:  352
N:  10 , choices:  724
N:  11 , choices:  2680
N:  12 , choices:  14200
N:  13 , choices:  73712
N:  14 , choices:  365596
'''



