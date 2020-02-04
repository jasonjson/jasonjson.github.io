---
layout: post
title: 1146 - Snapshot Array
date: 2020-02-04
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
Implement a SnapshotArray that supports the following interface:

* SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
* void set(index, val) sets the element at the given index to be equal to val.
* int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
* int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

```python
from bisect import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[[-1, 0]] for _ in range(length)] #(snap_id, val)
        self.snap_calls = 0


    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.snap_calls - 1, val])


    def snap(self) -> int:
        self.snap_calls += 1
        return self.snap_calls - 1


    def get(self, index: int, snap_id: int) -> int:
        i = bisect(self.array[index], [snap_id])
        return self.array[index][i - 1][1]
```
