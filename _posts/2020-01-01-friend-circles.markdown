---
layout: post
title: 547 - Friend Circles
date: 2020-01-01
tags:
- Leetcode
categories:
- Array
author: Jason
---
**There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends. Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.**

```python
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = [False] * len(M)
        ret = 0
        def dfs(i):
            for j in range(len(M[0])):
                if M[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)
        for i in range(len(M)):
            if not visited[i]:
                dfs(i)
                ret += 1
        return ret
```
