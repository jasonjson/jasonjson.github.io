---
layout: post
title: 385 - Mini Parser
date: 2017-11-07
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**Given a nested list of integers represented as a string, implement a parser to deserialize it. Each element is either an integer, or a list -- whose elements may also be integers or other lists.**


```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if not s:
            return
        if s[0] != "[":
            return NestedInteger(int(s))

        l = 0
        curr = None
        prev = []
        for r, char in enumerate(s):
            if char == "[":
                if curr:
                    prev.append(curr)
                curr = NestedInteger()
                l = r + 1
            elif char == "]":
                num = s[l: r]
                if num:
                    curr.add(NestedInteger(int(num)))
                if prev:
                    pop = prev.pop()
                    pop.add(curr)
                    curr = pop
                l = r + 1
            elif char == ",":
                if s[r - 1] != ']':
                    curr.add(NestedInteger(int(s[l: r])))
                l = r + 1
        return curr
```
