---
layout: post
title: Sudoku Solver
date: 2015-11-15 09:51:25.000000000 -05:00
tags: algorithm
categories:
- Brain teaser
- Matrix
author: Jason
---
<p><strong><em>Write a program to solve a Sudoku puzzle by filling the empty cells.</p>

Empty cells are indicated by the character '.'. You may assume that there will be only one unique solution.</em></strong></p>
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
