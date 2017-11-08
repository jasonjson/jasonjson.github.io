---
layout: post
title: 386 - Lexicographical Numbers
date: 2017-11-07
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given an integer n, return 1 - n in lexicographical order. For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].**


```python
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        ret = []
        curr = 1
        for i in xrange(1, n + 1):
            ret.append(curr)
            if curr * 10 <= n:
                curr *= 10
            elif curr % 10 != 9 and curr + 1 <= n:
                curr += 1
            else:
                while (curr / 10) % 10 == 9:
                    curr /= 10
                curr = curr / 10 + 1
        return ret
```
