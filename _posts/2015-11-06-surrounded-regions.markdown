---
layout: post
title: 130 - Surrounded Regions
date: 2015-11-06 22:47:03.000000000 -05:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in that surrounded region.**


``` java
public class Solution {
    public void solve(char[][] board) {
        if (board == null || board.length == 0) return ;
        int row = board.length, col = board[0].length;

        for (int i = 0; i < row; i++) {
            helper(board, i, 0);
            helper(board, i, col - 1);
        }
        for (int j = 0; j < col; j++) {
            helper(board, 0, j);
            helper(board, row - 1, j);
        }
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                board[i][j] = (board[i][j] == 'M' ? 'O' : 'X');
            }
        }
    }

    public void helper(char[][] board, int i, int j) {
        //transfer all non surrounded "O" to "M"
        if (board[i][j] == 'X' || board[i][j] == 'M') return;
        board[i][j] = 'M';
        if (i + 1 < board.length - 1) helper(board, i + 1, j);//最外面一层就不需要再回去了
        if (i - 1 > 0) helper(board, i - 1, j);
        if (j - 1 > 0) helper(board, i, j - 1);
        if (j + 1 < board[0].length - 1) helper(board, i, j + 1);
    }
}
```

``` python
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board:
            return

        row, col = len(board), len(board[0])
        for i in xrange(row):
            self.helper(i, 0, board)
            self.helper(i, col - 1, board)
        for j in xrange(col):
            self.helper(0, j, board)
            self.helper(row - 1, j, board)
        for i in xrange(row):
            for j in xrange(col):
                board[i][j] = "O" if board[i][j] == "M" else "X"

    def helper(self, i, j, board):
        if board[i][j] == "X" or board[i][j] == "M":
            return
        board[i][j] = "M"
        if i - 1 > 0:
            self.helper(i - 1, j, board)
        if i + 1 < len(board) - 1:
            self.helper(i + 1, j, board)
        if j - 1 > 0:
            self.helper(i, j - 1, board)
        if j + 1 < len(board[0]) - 1:
            self.helper(i, j + 1, board)
```
