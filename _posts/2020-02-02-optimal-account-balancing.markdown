---
layout: post
title: 465 - Optimal Account Balancing
date: 2020-02-02
tags:
- Leetcode
categories:
- Array
author: Jason
---
A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]]. Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.

```python
from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        value_map = defaultdict(int)
        for a, b, c in transactions:
            value_map[a] -= c
            value_map[b] += c

        debts = list(value_map.values())
        def dfs(start):
            while start < len(debts) and debts[start] == 0:
                start += 1
            if start == len(debts):
                return 0
            ret = float("inf")
            for i in range(start + 1, len(debts)):
                if debts[i] * debts[start] < 0:
                    debts[i] += debts[start]
                    ret = min(ret, dfs(start + 1) + 1)
                    debts[i] -= debts[start]
            return ret

        return dfs(0)
```
