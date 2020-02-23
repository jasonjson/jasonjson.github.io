---
layout: post
title: 79 - Word Search
date: 2015-10-21 14:39:43.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.**

``` python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        if not word:
            return True

        def helper(i, j, left):
            if not left:
                return True
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == left[0]:
                board[i][j] = "#"
                for new_i, new_j in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if helper(new_i, new_j, left[1:]):
                        return True
                board[i][j] = left[0]
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i, j, word):
                    return True
        return False
```
