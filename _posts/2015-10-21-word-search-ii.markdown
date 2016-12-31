---
layout: post
title: Word Search II
date: 2015-10-21 14:40:11.000000000 -04:00
type: post
published: true
status: publish
categories:
- Data Structure
- Dynamic Programming
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464027282;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:531;}i:1;a:1:{s:2:"id";i:1320;}i:2;a:1:{s:2:"id";i:1793;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A word can start from any position in the matrix and go left/right/up/down to the adjacent position.</em></strong></p>
<p>[expand title = "trie and dfs"]</p>
<pre>
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
     
     
    public ArrayList<string> wordSearchII(char[][] board, ArrayList<string> words) {
        // write your code here
        ArrayList<string> result = new ArrayList<string>();
        if (board == null || board.length == 0) return result;
        Trie trie = new Trie();
        for (String word : words) {
            trie.insert(word);
        }
        HashSet<string> set = new HashSet<>();
        boolean[][] visited = new boolean[board.length][board[0].length];
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                helper(board, i, j, trie, "", visited, set);
            }
        }
        result.addAll(set);
        return result;
    }
    
    public void helper(char[][] board, int i, int j, Trie trie, String path, boolean[][] visited, HashSet<string> set) {
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
</string></string></string></string></string></string></pre>
<p>[/expand]</p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public ArrayList<string> wordSearchII(char[][] board, ArrayList<string> words) {
        ArrayList<string> result = new ArrayList<string>();
        if (board == null || board.length == 0 || words == null || words.size() == 0) return result;        
        for (String word : words) {
            if (exist(board, word)) {
                result.add(word);
            }
        }
        return result;
    }    
    public boolean exist(char[][] board, String word) {
        int row = board.length, col = board[0].length;
        boolean[][] visited = new boolean[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
            //each time a brand new visited is passed to find method
                if (find(board, i, j, word, 0, visited)) {
                    return true;
                }
            }
        }
        return false;
    }    
    public boolean find(char[][] board, int i, int j, String word, int start, boolean[][] visited) {
        if (start == word.length()) return true;
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || visited[i][j] || board[i][j] != word.charAt(start)) {
            return false;
        }
        visited[i][j] = true;//we don't want to modify the original matrix, but we can't use board[i][j] in following search, so we mark it visited
        if (find(board, i+1, j, word, start + 1, visited) || find(board, i - 1, j, word, start + 1, visited) || find(board, i, j + 1, word, start + 1, visited) || find(board, i , j - 1, word, start + 1, visited)) {
            return true;
        }
        visited[i][j] = false;
        return false;
    }
</string></string></string></string></pre>
<p>[/expand]</p>
