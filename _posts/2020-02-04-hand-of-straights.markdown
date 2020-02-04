---
layout: post
title: 846 - Hand Of Straights
date: 2020-02-04
tags:
- Leetcode
categories:
- Array
author: Jason
---
Alice has a hand of cards, given as an array of integers. Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards. Return true if and only if she can.

```python
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if W > len(hand) or len(hand) % W != 0:
            return False

        counter = Counter(hand)
        for c in sorted(counter):
            if counter[c] > 0:
                curr = counter[c]
                for i in range(W):
                    counter[c + i] -= curr
                    if counter[c + i] < 0:
                        return False
        return True
```
