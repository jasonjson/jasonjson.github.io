---
layout: post
title: 348 - Design Tic Tac Toe
date: 2020-01-16
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
Design a Tic-tac-toe game that is played between two players on a n x n grid. You may assume the following rules:

* A move is guaranteed to be valid and is placed on an empty block.
* Once a winning condition is reached, no more moves is allowed.
* A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

```python
class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        offset = 1 if player == 1 else -1
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diag += offset
        if row + col == self.n - 1:
            self.anti_diag += offset
        if offset * self.n in (self.row[row], self.col[col], self.diag, self.anti_diag):
            return player
        return 0
```
