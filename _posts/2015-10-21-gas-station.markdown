---
layout: post
title: 134 - Gas Station
date: 2015-10-21 14:14:07.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**There are N gas stations along a circular route, where the amount of gas at station i is gas[i]. You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations. Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.**

``` python
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        if not gas or not cost:
            return -1

        left_gas = index = 0
        for i in range(len(gas)):
            left_gas += gas[i] - cost[i]
            if left_gas < 0:
                left_gas = 0
                index = i + 1
        return index if sum(gas) >= sum(cost) else -1
```
