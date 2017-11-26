---
layout: post
title: 277 - Find the Celebrity
date: 2015-10-29 14:57:47.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them. Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense). You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.**


``` python
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in xrange(n):
            if knows(candidate, i):
                candidate = i
        for i in xrange(candidate):
            if knows(candidate, i):
                return -1
        for i in xrange(n):
            if not knows(i, candidate):
                return -1
        return candidate
```
