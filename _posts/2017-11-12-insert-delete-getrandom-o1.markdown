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
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.index_map:
            self.nums.append(val)
            self.index_map[val] = len(self.nums) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        if val in self.index_map:
            index, last = self.index_map[val], self.nums[-1]
            self.index_map[last], self.nums[index] = index, last
            self.nums.pop()
            del self.index_map[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)
```
