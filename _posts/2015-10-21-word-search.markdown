---
layout: post
title: Word Search
date: 2015-10-21 14:39:43.000000000 -04:00
type: post
published: true
status: publish
categories:
- Dynamic Programming
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465419352;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:583;}i:1;a:1:{s:2:"id";i:1506;}i:2;a:1:{s:2:"id";i:450;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param board: A list of lists of character
     * @param word: A string
     * @return: A boolean
     */
    public boolean exist(char[][] board, String word) {
        // write your code here
        if (board == null || board.length == 0) return false;
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (helper(board, i, j, word)) {
                    return true;
                }
            }
        }
        return false;
    }   
    public boolean helper(char[][] board, int i, int j, String word) {
        if (word.length() == 0) {
            return true;
        }//this must come first!!!, the last char be be at the edge and thus i j might be out of border
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length) {
            return false;
        }
        if (word.charAt(0) == board[i][j]) {
            board[i][j] = '#';
            if (helper(board, i + 1, j, word.substring(1)) || helper(board, i - 1, j, word.substring(1)) || helper(board, i, j + 1, word.substring(1)) || helper(board, i, j - 1, word.substring(1))) {
                return true;
            }
            board[i][j] = word.charAt(0);
        }
        return false;
    }
}
</pre>
<p>[/expand]</p>
