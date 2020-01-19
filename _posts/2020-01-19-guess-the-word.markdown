---
layout: post
title: 843 - Guess The Word
date: 2020-01-19
tags:
- Leetcode
categories:
- Array
author: Jason
---
We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as secret. You may call master.guess(word) to guess a word.  The guessed word should have type string and must be from the original list with 6 lowercase letters. This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word.  Also, if your guess is not in the given wordlist, it will return -1 instead.

```python
from collections import defaultdict
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        if not wordlist:
            return

        def cal_matches(a, b):
            return sum(s1 == s2 in zip(a, b))

        while wordlist:
            candidate = self.most_overlap(wordlist)
            matches = master.guess(candidate)
            if matches == 6:
                return
            wordlist = [w for w in wordlist if cal_matches(candidate, w) == matches]

    def most_overlap(self, candidates):
        counts = [defaultdict(int) for _ in range(6)]
        for word in candidates:
            for i, c in enumerate(word):
                counts[i][c] += 1
        return max(candidates, key=lambda x: sum(counts[i][c] for i, c in enumerate(x)))
```
