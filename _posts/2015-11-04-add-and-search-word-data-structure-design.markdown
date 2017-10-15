---
layout: post
title: 211 - Add and Search Word
date: 2015-11-04 11:39:30.000000000 -05:00
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**Design a data structure that supports the following two operations:**
* void addWord(word)
* bool search(word)
**search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.**


``` java
public class WordDictionary {
    class TrieNode {
        boolean storeWord = false;
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
            curr.storeWord = true;
        }
        public boolean search(String word, TrieNode curr) {
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                if (c == '.') {
                    for (TrieNode temp : curr.children) {
                        if (temp != null && search(word.substring(i+1), temp)) {
                            return true;//search the rest chars, do not start from beginning
                        }
                    }
                    return false;
                } else {
                    if (curr.children[c - 'a'] == null) {
                        return false;
                    }
                    curr = curr.children[c - 'a'];
                }
            }
            return curr.storeWord;
        }
    }
    Trie trie = new Trie();
    // Adds a word into the data structure.
    public void addWord(String word) {
        trie.insert(word);
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) {
        return trie.search(word, trie.root);
    }
}
```

``` python
class TrieNode(object):

    def __init__(self):
        self.is_word = False
        self.char_map = {}

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            if char not in curr.char_map:
                curr.char_map[char] = TrieNode()
            curr = curr.char_map[char]
        curr.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        return self.helper(curr, word)

    def helper(self, root, word):
        for i, char in enumerate(word):
            if char == ".":
                for child in root.char_map.values():
                    if self.helper(child, word[i + 1:]):
                        return True
                return False
            elif char not in root.char_map:
                return False
            root = root.char_map[char]
        return root.is_word
```
