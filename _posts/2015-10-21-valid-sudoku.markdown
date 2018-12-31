---
layout: post
title: 36 - Valid Sudoku
date: 2015-10-21 13:02:11.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Determine whether a Sudoku is valid.The Sudoku board could be partially filled, where empty cells are filled with the character '.'**


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

``` python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        if not board:
            return False

        for i in range(9):
            s1, s2 = set(), set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in s1:
                    return False
                if board[j][i] != "." and board[j][i] in s2:
                    return False
                s1.add(board[i][j])
                s2.add(board[j][i])
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s3 = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] != "." and board[k][l] in s3:
                            return False
                        s3.add(board[k][l])
        return True
```
