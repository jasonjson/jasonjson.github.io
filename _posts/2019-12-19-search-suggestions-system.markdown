---
layout: post
title: 1268 - Search Suggestions System
date: 2019-12-19
tags:
- Leetcode
categories:
- Data structure
author: Jason
---

```python
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        if not products or not searchWord:
            return []
        trie = Trie()
        for word in products:
            trie.insert(word)
        return trie.find(searchWord)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.words.append(word)

    def find(self, word):
        ret = []
        curr = self.root
        for char in word:
            if char not in curr.children:
                break
            curr = curr.children[char]
            ret.append(sorted(curr.words)[:3])

        for i in range(len(word) - len(ret)):
            ret.append([])
        return ret
```
