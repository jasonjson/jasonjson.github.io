---
layout: post
title: Beautiful Arrangement
date: 2017-06-13
tags:
- Algorithm
categories:
- DFS BACKTRACKING
author: Jason
---
**Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 ≤ i ≤ N) in thisarray: The number at the ith position is divisible by i. i is divisible by the number at the ith position. Now given N, how many beautiful arrangements can you construct?**

```python
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache = {}
        return self.helper(N, tuple(range(1, N + 1)), cache)

    def helper(self, i, X, cache):
        if i == 1:
            return 1
        key = (i, X)
        if key in cache:
            return cache[key]
        total = 0
        for index, num in enumerate(X):
            if num % i == 0 or i % num == 0:
                total += self.helper(i - 1, X[:index] + X[index+1:], cache)
        cache[key] = total
        return total

class Solution(object):
    def countArrangement(self, N):
        ret = [0]
        visited = [0] * (N + 1)
        self.helper(N, visited, 1, ret)
        return ret[0]

    def helper(self, N, visited, position, ret):
        if position > N:
            ret[0] += 1
            return
        for i in range(1, N + 1):
            if not visited[i] and (i % position == 0 or position % i == 0):
                visited[i] = 1
                self.helper(N, visited, position + 1, ret)
                visited[i] = 0
```
