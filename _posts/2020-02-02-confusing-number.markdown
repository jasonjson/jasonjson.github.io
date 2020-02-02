---
layout: post
title: 1056 - Confusing Number
date: 2020-02-02
tags:
- Leetcode
categories:
- Integer
author: Jason
---
Given a number N, return true if and only if it is a confusing number, which satisfies the following condition: We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid. A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

```python
class Solution:
    def confusingNumber(self, N: int) -> bool:
        rotation_dict = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        rotation = ""
        for c in str(N):
            if c not in rotation_dict:
                return False
            rotation += rotation_dict[c]

        return str(N) != rotation[::-1]
```
