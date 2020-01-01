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


``` java
public class Solution {
    class TrieNode {
        boolean isWord = false;
        TrieNode[] children = new TrieNode[26];
    }
    class Trie {
        TrieNode root = new TrieNode();
        public void insert(String word) {
            TrieNode curr = root;
            for (char c : word.toCharArray()) {
                if (curr.children[c - 'a'] == null) {
                    curr.children[c - 'a'] = new TrieNode();
                }
                curr = curr.children[c - 'a'];
            }
            curr.isWord = true;
        }

        public boolean startsWith(String prefix) {
            TrieNode curr = root;
            for (char c : prefix.toCharArray()) {
                if (curr.children[c - 'a'] == null) {
                    return false;
                }
                curr = curr.children[c - 'a'];
            }
            return true;
        }

        public boolean search(String word) {
            TrieNode curr = root;
            for (char c : word.toCharArray()) {
                if (curr.children[c - 'a'] == null) {
                    return false;
                }
                curr = curr.children[c - 'a'];
            }
            return curr.isWord;
        }
    }


    public ArrayList<String> wordSearchII(char[][] board, ArrayList<String> words) {
        // write your code here
        ArrayList<String> result = new ArrayList<String>();
        if (board == null || board.length == 0) return result;
        Trie trie = new Trie();
        for (String word : words) {
            trie.insert(word);
        }
        HashSet<String> set = new HashSet<>();
        boolean[][] visited = new boolean[board.length][board[0].length];
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                helper(board, i, j, trie, "", visited, set);
            }
        }
        result.addAll(set);
        return result;
    }

    public void helper(char[][] board, int i, int j, Trie trie, String path, boolean[][] visited, HashSet<String> set) {
        if (trie.search(path)) {
            set.add(new String(path));
        }
        if (trie.startsWith(path) && !visited[i][j]) {
            path += board[i][j];
            visited[i][j] = true;
            if (i - 1 >= 0) helper(board, i - 1, j, trie, path, visited, set);
            if (i + 1 < board.length) helper(board, i + 1, j, trie, path, visited, set);
            if (j - 1 >= 0) helper(board, i, j - 1, trie, path, visited, set);
            if (j + 1 < board[0].length) helper(board, i, j + 1, trie, path, visited, set);
            visited[i][j] = false;
            path = path.substring(0, path.length() - 1);
        }
    }
}
```

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
