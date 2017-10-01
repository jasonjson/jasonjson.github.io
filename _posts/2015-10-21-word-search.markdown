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


``` java
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
```

``` python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.helper(board, i, j, 0, word):
                    return True
        return False

    def helper(self, board, i, j, index, word):
        if index == len(word):
            return True
        if i in xrange(len(board)) and j in xrange(len(board[0])) and board[i][j] == word[index]:
            board[i][j] = "#"
            if self.helper(board, i + 1, j, index + 1, word) or self.helper(board, i - 1, j, index + 1, word) or self.helper(board, i, j + 1, index + 1, word) or self.helper(board, i, j - 1, index + 1, word):
                return True
            board[i][j] = word[index]
        return False
```
