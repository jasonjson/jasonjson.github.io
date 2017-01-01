---
layout: post
title: Valid Sudoku
date: 2015-10-21 13:02:11.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464843101;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1050;}i:1;a:1:{s:2:"id";i:1506;}i:2;a:1:{s:2:"id";i:583;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Determine whether a Sudoku is valid.The Sudoku board could be partially filled, where empty cells are filled with the character ..</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public boolean isValidSudoku(char[][] board) {
        if (board == null || board.length == 0) return true;
        
        int n = board.length;
        Set<character> s1, s2;
        for (int i = 0; i < n; i++) {
            s1 = new HashSet<character>();
            s2 = new HashSet<character>();
            for (int j = 0; j < n; j++) {
                if (!s1.add(board[i][j]) && board[i][j] != '.') {
                    return false;
                }
                if (!s2.add(board[j][i]) && board[j][i] != '.') {
                    return false;
                }
            }
        }
        for (int i = 0; i < n; i += 3) {
            for (int j = 0; j < n; j+= 3) {
                s1 = new HashSet<character>();
                for (int l = i; l < i + 3; l++) {
                    for (int k = j; k < j + 3; k++) {
                        if (!s1.add(board[l][k]) && board[l][k] != '.') {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }
}
</character></character></character></character></pre>
<p>[/expand]</p>
