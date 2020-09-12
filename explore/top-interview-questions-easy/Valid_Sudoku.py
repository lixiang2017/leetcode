'''
You are here!
Your runtime beats 82.33 % of python submissions.
'''



class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        row = [{} for i in range(9)]
        column = [{} for i in range(9)]
        box = [{} for i in range(9)]

        # validate a value
        for i in range(9):
        	for j in range(9):
        		if board[i][j] != '.':
        			num = int(board[i][j])
        			box_index = (i // 3) * 3 + j / 3

        			# update hash tables
        			row[i][num] = row[i].get(num, 0) + 1
        			column[j][num] = column[j].get(num, 0) + 1
        			box[box_index][num] = box[box_index].get(num, 0) + 1

        			# check if this value has been seen before
        			if row[i][num] > 1 or column[j][num] > 1 or box[box_index][num] > 1:
        				return False

        return True


if __name__ == '__main__':
	board = [
	  ["5","3",".",".","7",".",".",".","."],
	  ["6",".",".","1","9","5",".",".","."],
	  [".","9","8",".",".",".",".","6","."],
	  ["8",".",".",".","6",".",".",".","3"],
	  ["4",".",".","8",".","3",".",".","1"],
	  ["7",".",".",".","2",".",".",".","6"],
	  [".","6",".",".",".",".","2","8","."],
	  [".",".",".","4","1","9",".",".","5"],
	  [".",".",".",".","8",".",".","7","9"]
	]
	assert Solution().isValidSudoku(board)

	board = [
	  ["8","3",".",".","7",".",".",".","."],
	  ["6",".",".","1","9","5",".",".","."],
	  [".","9","8",".",".",".",".","6","."],
	  ["8",".",".",".","6",".",".",".","3"],
	  ["4",".",".","8",".","3",".",".","1"],
	  ["7",".",".",".","2",".",".",".","6"],
	  [".","6",".",".",".",".","2","8","."],
	  [".",".",".","4","1","9",".",".","5"],
	  [".",".",".",".","8",".",".","7","9"]
	]
assert not Solution().isValidSudoku(board)

