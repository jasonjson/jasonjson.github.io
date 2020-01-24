---
layout: post
title: 37 - Sudoku Solver
date: 2015-11-15 09:51:25.000000000 -05:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**Write a program to solve a Sudoku puzzle by filling the empty cells.Empty cells are indicated by the character '.'. You may assume that there will be only one unique solution.**


``` java
public class Solution {
    public void solveSudoku(char[][] board) {
        if (board == null || board.length == 0) return;
        helper(0, board);
    }

    public boolean helper(int start, char[][] board) {
        if (start == 81) return true;
        int i = start / 9, j = start % 9;// row: division; col: modulus
        if (board[i][j] != '.') {
            return helper(start + 1, board);
        } else {
            for (char c = '1'; c <= '9'; c++) {
                if (isValid(board, i, j, c)) {
                    board[i][j] = c;
                    if (helper(start + 1, board)) {
                        return true;
                    }
                    board[i][j] = '.';
                }
            }
            return false;
        }
    }

    public boolean isValid(char[][] board, int i, int j, char c) {
        for (int k = 0; k < 9; k++) {
            if (board[i][k] == c || board[k][j] == c || board[i - i % 3 + k / 3][j - j % 3 + k % 3] == c) {
                return false;
            }
        }
        return true;
    }
}
```

``` python
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

        i, j = start // 9, start % 9
        if board[i][j] != ".":
            return self.helper(start + 1, board)
        else:
            for x in range(1, 10):
                if self.is_valid(board, i, j, str(x)):
                    board[i][j] = str(x)
                    if self.helper(start + 1, board):
                        return True
                    board[i][j] = "."
            return False

    def is_valid(self, board, i, j , x):
        for k in range(9):
            if x in (board[i][k], board[k][j], board[i - i % 3 + k / 3][j - j % 3 + k % 3]):
                return False
        return True
```
