---
layout: post
title: 289 - Game of Life
date: 2015-10-28 15:02:31.000000000 -04:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):**
* Any live cell with fewer than two live neighbors dies, as if caused by under-population.
* Any live cell with two or three live neighbors lives on to the next generation.
* Any live cell with more than three live neighbors dies, as if by over-population.
* Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
**Write a function to compute the next state (after one update) of the board given its current state.**
[Reference](http://www.cnblogs.com/grandyang/p/4854466.html)

* 0 -> 0 : die to die
* 1 -> 1 : live to live
* 1 -> 2 : live to die
* 0 -> 3 : die to live

``` java
public class Solution {
    public void gameOfLife(int[][] board) {
        if (board == null || board.length == 0) return;

        int row = board.length, col = board[0].length;
        int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                int count = 0;
                for (int k = 0; k < 8; k++) {
                    int newX = i + dx[k], newY = j + dy[k];
                    if (newX >= 0 && newX < row && newY >= 0 && newY < col && (board[newX][newY] == 1 || board[newX][newY] == 2)) {
                        count ++;
                    }
                }
                if (board[i][j] == 1 && (count < 2 || count > 3)) {
                    board[i][j] = 2;
                } else if (board[i][j] == 0 && count == 3) {
                    board[i][j] = 3;
                }
            }
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                board[i][j] %= 2;
            }
        }
    }
}
```

``` python
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board:
            return

        row, col = len(board), len(board[0])
        for i in xrange(row):
            for j in xrange(col):
                count = self.count_live(board, i, j)
                if board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = 2
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = 3
        for i in xrange(row):
            for j in xrange(col):
                board[i][j] %= 2

    def count_live(self, board, i, j):
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        count = 0
        for k in xrange(8):
            new_i = i + dx[k]
            new_j = j + dy[k]
            if new_i >= 0 and new_i < len(board) and new_j >= 0 and new_j < len(board[0]) and board[new_i][new_j] in [1, 2]:
                count += 1
        return count
```
