---
layout: post
title: 1429 - First Unique Number
date: 2022-06-10
tags:
- Leetcode
categories:
- Array
author: Jason
---
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

1. FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
2. int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
3. void add(int value) insert value to the queue.

```cpp
from collections import Counter
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.counters = Counter(nums)
        self.nums = nums
        self.last_index = 0

    def showFirstUnique(self) -> int:
        for i in range(self.last_index, len(self.nums)):
            if self.counters[self.nums[i]] == 1:
                self.last_index = i
                return self.nums[i]
        self.last_index = len(self.nums)
        return -1;

    def add(self, value: int) -> None:
        self.counters[value] += 1
        if (self.counters[value] == 1):
            self.nums.append(value)
```
