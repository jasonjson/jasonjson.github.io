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

        size = len(board)
        for i in xrange(size):
            nums1, nums2 = [], []
            for j in xrange(size):
                if board[i][j] != "." and board[i][j] in nums1:
                    return False
                if board[j][i] != "." and board[j][i] in nums2:
                    return False
                nums1.append(board[i][j])
                nums2.append(board[j][i])
        for i in xrange(0, size, 3):
            for j in xrange(0, size, 3):
                nums3 = []
                for k in xrange(i, i + 3):
                    for l in xrange(j, j + 3):
                        if board[k][l] != "." and board[k][l] in nums3:
                            return False
                        nums3.append(board[k][l])
        return True
```
