---
layout: post
title: Valid Sudoku
date: 2015-10-21 13:02:11.000000000 -04:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Determine whether a Sudoku is valid.The Sudoku board could be partially filled, where empty cells are filled with the character ..</em></strong></p>


``` java
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
```
