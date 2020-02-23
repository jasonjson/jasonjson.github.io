---
layout: post
title: 212 - Word Search II
date: 2015-10-21 14:40:11.000000000 -04:00
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A word can start from any position in the matrix and go left/right/up/down to the adjacent position.**

``` python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        trie = Trie()
        for word in words:
            trie.insert(word)
        ret = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.helper(board, i, j, trie.root, "", ret)
        return ret

    def helper(self, board, i, j, curr, path, ret):
        if curr.is_word:
            ret.append(path)
            curr.is_word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in curr.children:
            return
        tmp = board[i][j]
        curr = curr.children[tmp]
        board[i][j] = "#"
        path += tmp
        self.helper(board, i + 1, j, curr, path, ret)
        self.helper(board, i - 1, j, curr, path, ret)
        self.helper(board, i, j - 1, curr, path, ret)
        self.helper(board, i, j + 1, curr, path, ret)
        path = path[:-1]
        board[i][j] = tmp
```
