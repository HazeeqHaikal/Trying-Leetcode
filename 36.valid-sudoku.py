#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (58.48%)
# Likes:    9336
# Dislikes: 969
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
#
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
# without repetition.
#
#
# Note:
#
#
# A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
# Only the filled cells need to be validated according to the mentioned
# rules.
#
#
#
# Example 1:
#
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#
#
# Example 2:
#
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it
# is invalid.
#
#
#
# Constraints:
#
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
#
#
#

# @lc code=start
from collections import defaultdict


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool

        Time complexity: O(1)
        Space complexity: O(1)
        """

        # example input
        # board = [
        #     [5, 3, ., ., 7, ., ., ., .],
        #     [6, ., ., 1, 9, 5, ., ., .],
        #     [., 9, 8, ., ., ., ., 6, .],
        #     [8, ., ., ., 6, ., ., ., 3],
        #     [4, ., ., 8, ., 3, ., ., 1],
        #     [7, ., ., ., 2, ., ., ., 6],
        #     [., 6, ., ., ., ., 2, 8, .],
        #     [., ., ., 4, 1, 9, ., ., 5],
        #     [., ., ., ., 8, ., ., 7, 9]
        # ]

        # using hashet
        # unique hashset for every single row in entire 9x9
        # unique hashset for every single column

        column = defaultdict(set)
        row = defaultdict(set)
        # key (row/3, column/3)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in row[r]
                    or board[r][c] in column[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                column[c].add(board[r][c])
                row[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

        # init data
        # rows = [{} for i in range(9)]
        # columns = [{} for i in range(9)]
        # boxes = [{} for i in range(9)]

        # # validate a board
        # for i in range(9):
        #     for j in range(9):
        #         num = board[i][j]
        #         if num != '.':
        #             # check if the num is already in the current row
        #             if num in rows[i]:
        #                 return False
        #             else:
        #                 rows[i][num] = 1
        #             # check if the num is already in the current column
        #             if num in columns[j]:
        #                 return False
        #             else:
        #                 columns[j][num] = 1
        #             # check if the num is already in the current box
        #             box_index = (i // 3) * 3 + j // 3
        #             if num in boxes[box_index]:
        #                 return False
        #             else:
        #                 boxes[box_index][num] = 1
        # return True


# @lc code=end
