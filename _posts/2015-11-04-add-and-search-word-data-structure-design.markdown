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
Design a data structure that supports the following two operations, search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

* void addWord(word)
* bool search(word)

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

    def find(self, word, curr):
        for i, c in enumerate(word):
            if c == ".":
                for next_node in curr.children.values():
                    if self.find(word[i+1:], next_node):
                        return True
                return False
            elif c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.is_word

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.trie.find(word, self.trie.root)
```
