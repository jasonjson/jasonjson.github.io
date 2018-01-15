#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        self.helper(0, board)

    def helper(self, start, board):
        if start == 81:
            return True

        i, j = start / 9, start % 9
        if board[i][j] != ".":
            return self.helper(start + 1, board)
        else:
            for candidate in xrange(1, 10):
                if self.is_valid(board, i, j, str(candidate)):
                    board[i][j] = str(candidate)
                    if self.helper(start + 1, board):
                        return True
                    board[i][j] = "."
            return False

    def is_valid(self, board, i, j , candidate):
        print i, j, candidate
        for k in xrange(9):
            if board[i][k] == candidate or board[k][j] == candidate or board[i - i % 3 + k /3 ][j - j %3 + k % 3] == candidate:
                return False
        return True
if __name__ == "__main__":
    solution = Solution()
    board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    solution.solveSudoku(board)
    __import__('pprint').pprint(board)
