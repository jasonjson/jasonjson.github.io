---
layout: post
title: 957 - Prison Cells After N Days
date: 2020-01-20
tags:
- Leetcode
categories:
- Array
author: Jason
---
There are 8 prison cells in a row, and each cell is either occupied or vacant. Each day, whether the cell is occupied or vacant changes according to the following rules:

* If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
* Otherwise, it becomes vacant.

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0. Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

```python
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # use a dict to find the size of the pattern
        N %= 14
        if N % 14 == 0:
            N = 14
        for _ in range(N):
            tmp = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    tmp[i] = 1
            cells = tmp
        return cells
```
