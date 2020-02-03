---
layout: post
title: 299 - Bulls and Cows
date: 2015-10-31 20:21:40.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**You are playing the following Bulls and Cows game with your friend: You write a 4-digit secret number and ask your friend to guess it, each time your friend guesses a number, you give a hint, the hint tells your friend how many digits are in the correct positions (called "bulls") and how many digits are in the wrong positions (called "cows"), your friend will use those hints to find out the secret number.**

``` python
from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        char_dict = defaultdict(int)
        cows = bulls = 0
        for c1, c2 in zip(secret, guess):
            if c1 == c2:
                bulls += 1
            else:
                if char_dict[c1] < 0:
                    cows += 1
                if char_dict[c2] > 0:
                    cows += 1
                char_dict[c1] += 1
                char_dict[c2] -= 1

        return str(bulls) + "A" + str(cows) + "B"
```
