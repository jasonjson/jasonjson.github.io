---
layout: post
title: 341 - Flatten Nested List Iterator
date: 2020-01-09
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**Given a nested list of integers, implement an iterator to flatten it. Each element is either an integer, or a list -- whose elements may also be integers or other lists.**


```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list = self.flatten_list(nestedList)

    def flatten_list(self, nestedList):
        ret = []
        for nested_integer in nestedList:
            if nested_integer.isInteger():
                ret.append(nested_integer.getInteger())
            else:
                ret.extend(self.flatten_list(nested_integer.getList()))
        return ret

    def next(self):
        """
        :rtype: int
        """
        return self.list.pop(0)


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.list
```

``` python
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]


    def next(self) -> int:
        self.hasNext()
        nestedList, index = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[index].getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            nestedList, index = self.stack[-1]
            if index == len(nestedList):
                self.stack.pop()
            else:
                nestedInteger = nestedList[index]
                if nestedInteger.isInteger():
                    return True
                self.stack[-1][1] += 1
                self.stack.append([nestedInteger.getList(), 0])
        return False
```
