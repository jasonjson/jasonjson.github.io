---
layout: post
title: 282 - Expression Add Operators
date: 2015-10-28 12:58:06.000000000 -04:00
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
**Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.**
[reference](http://segmentfault.com/a/1190000003797204")

``` python
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []

        ret = []
        self.helper(num, target, 0, 0, [], ret)
        return ret

    def helper(self, num, target, sums, prev, path, ret):
        if len(num) == 0:
            if sums == target:
                ret.append("".join(path))
            return
        for i in range(1, len(num) + 1):
            if num[0] == "0" and i > 1:
                continue
            n = int(num[:i])
            if not path:
                self.helper(num[i:], target, n, n, [str(n)], ret)
            else:
                self.helper(num[i:], target, sums + n, n, path + ["+", str(n)], ret)
                self.helper(num[i:], target, sums - n, -n, path + ["-", str(n)], ret)
                self.helper(num[i:], target, sums + prev * n - prev, prev * n, path + ["*", str(n)], ret)
```
