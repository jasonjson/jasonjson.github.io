---
layout: post
title: 773 - Sliding Puzzle
date: 2020-01-20
tags:
- Leetcode
categories:
- Array
author: Jason
---
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it. The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]]. Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

```python
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        if not board:
            return 0

        s = "".join(str(board[i][j]) for i in range(2) for j in range(3))
        visited = {s}
        prev = [s]
        step = 0
        while prev:
            curr = []
            for b in prev:
                visited.add(b)
                if b == "123450":
                    return step
                for move in self.find_next(b):
                    if move not in visited:
                        curr.append(move)
            step += 1
            prev = curr
        return -1

    def find_next(self, s):
        ret = []
        zero = s.index("0")
        i, j = zero // 3, zero % 3
        for new_i, new_j in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
            if 0 <= new_i < 2 and 0 <= new_j < 3:
                s_list = list(s)
                s_list[zero], s_list[new_i * 3 + new_j] = s_list[new_i * 3 + new_j], s_list[zero]
                ret.append("".join(s_list))
        return ret
```
