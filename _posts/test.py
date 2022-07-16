#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if startRow < 0 or startRow >= m or startColumn < 0 or startColumn >= n:
            return 1
        elif maxMove == 0:
            return 0
        else:
            a = self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn)
            b = self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn)
            c = self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1)
            d = self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1)
            return a + b + c + d

s = Solution()
print(s.findPaths(2, 2, 2, 0, 0))
print(s.findPaths(1, 3, 3, 0, 1))
