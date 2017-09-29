---
layout: post
title: Hamming Distance
date: 2017-04-26
tags:
- Algorithm
categories:
- Brain Teaser
author: Jason
---
**The Hamming distance between two integers is the number of positions at which the corresponding bits are different. Given two integers x and y, calculate the Hamming distance.**

```python
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_binary = self.to_binary(x)
        y_binary = self.to_binary(y)
        size_diff = len(x_binary) - len(y_binary)
        if size_diff > 0:
            y_binary.extend([0] * size_diff)
        else:
            x_binary.extend([0] * (-size_diff))
        dist = 0
        for i, j in zip(x_binary, y_binary):
            if i != j:
                dist += 1
        return dist

    def to_binary(self, x):
        result = []
        while x != 0:
            result.append(x % 2)
            x //= 2
        return result
```

```python
class Solution(object):
    def hammingDistance(self, x, y):
        #bin: convert a int to binary string
        return bin(x^y).count("1")
```
