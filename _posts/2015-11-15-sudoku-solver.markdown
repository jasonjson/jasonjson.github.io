---
layout: post
title: Sudoku Solver
date: 2015-11-15 09:51:25.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Matrix
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463330490;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:583;}i:1;a:1:{s:2:"id";i:450;}i:2;a:1:{s:2:"id";i:581;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Write a program to solve a Sudoku puzzle by filling the empty cells.<br />
Empty cells are indicated by the character '.'. You may assume that there will be only one unique solution.</em></strong></p>
<p>[expand title = "O(1) space"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
