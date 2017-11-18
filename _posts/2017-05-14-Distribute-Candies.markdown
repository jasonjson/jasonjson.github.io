---
layout: post
title: 575 - Distribute Candies
date: 2017-05-14
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.**

```python
from collections import Counter
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        count = Counter(candies)
        #always can give all different kinds of candies to sister
        return min(len(candies) // 2, len(count))
```
