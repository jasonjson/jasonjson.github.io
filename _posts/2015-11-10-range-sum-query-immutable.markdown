---
layout: post
title: 303 - Range Sum Query - Immutable
date: 2015-11-10 09:14:36.000000000 -05:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.**


``` java
public class NumArray {
    int[] sums;
    public NumArray(int[] nums) {
        sums = new int[nums.length + 1];
        for (int i = 1; i <= nums.length; i++) {
            sums[i] = sums[i - 1] + nums[i - 1];
        }
    }

    public int sumRange(int i, int j) {
        return sums[j + 1] - sums[i];
    }
}
```

``` python
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = [0]
        for num in nums:
            self.sums.append(self.sums[-1] + num)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j + 1] - self.sums[i]
```
