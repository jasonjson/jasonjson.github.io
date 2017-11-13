---
layout: post
title: 380 - Insert Delete Getrandom O1
date: 2017-11-12
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**Design a data structure that supports all following operations in average O(1) time.**

* insert(val): Inserts an item val to the set if not already present.
* remove(val): Removes an item val from the set if present.
* getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.


```python
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = []
        self.index = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            self.num.append(val)
            self.index[val] = len(self.num) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            index, last = self.index[val], self.num[-1]
            self.num[index] = last
            self.index[last] = index
            self.index.pop(val)
            self.num.pop()
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.num[random.randint(0, len(self.num) - 1)]
```
