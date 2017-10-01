---
layout: post
title: Surrounded Regions
date: 2015-11-06 22:47:03.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
<p><strong><em>Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.</p>

A region is captured by flipping all 'O's into 'X's in that surrounded region.</em></strong></p>
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
