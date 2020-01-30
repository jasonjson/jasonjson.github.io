---
layout: post
title: 256 - Paint House
date: 2015-10-31 11:26:50.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

``` python
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        return min(costs[-1])
```
