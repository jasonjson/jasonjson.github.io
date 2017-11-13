---
layout: post
title: 381 - Insert Delete Getrandom O1 Duplicates Allowed
date: 2017-11-12
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**Design a data structure that supports all following operations in average O(1) time. Note: Duplicate elements are allowed.**

* insert(val): Inserts an item val to the collection.
* remove(val): Removes an item val from the collection if present.
* getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.


```python
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = []
        self.index = collections.defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.num.append(val)
        self.index[val].add(len(self.num) - 1)
        return len(self.index[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        index_list = self.index[val]
        if index_list:
            index, last = index_list.pop(), self.num[-1]
            self.num[index] = last #its possible the last item is val
            self.index[last].add(index)
            self.index[last].discard(len(self.num) - 1)
            self.num.pop()
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.num[random.randint(0, len(self.num) - 1)]
```
