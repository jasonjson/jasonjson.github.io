---
layout: post
title: 642 - Design Search Autocomplete System
date: 2019-12-27
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:**

1. The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
2. The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
3. If less than 3 hot sentences exist, then just return as many as you can.
4. When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

```python
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = defaultdict(int)

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = self.curr = TrieNode()
        self.sentence = ""
        for sentence, time in zip(sentences, times):
            self.insert(sentence, time)

    def insert(self, sentence, time):
        curr = self.root
        for c in sentence:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.words[sentence] += time

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.curr = self.root
            self.insert(self.sentence, 1)
            self.sentence = ""
            return []
        self.sentence += c
        if c not in self.curr.children:
            #create a dummy node for following input
            self.curr = TrieNode()
            return []
        else:
            self.curr = self.curr.children[c]
            candidates = sorted(self.curr.words.items(), key=lambda item: (-item[1], item[0]))
            return [v[0] for v in candidates[:3]]
```
