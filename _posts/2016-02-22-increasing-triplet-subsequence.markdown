---
layout: post
title: 334 - Increasing Triplet Subsequence
date: 2016-02-22 23:25:30.000000000 -05:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.**


``` java
public class Solution {
    public boolean increasingTriplet(int[] nums) {
        if (nums == null || nums.length == 0) return false;

        int min = Integer.MAX_VALUE, secondMin = Integer.MAX_VALUE;
        for (int num : nums) {
            if (num <= min) {
                min = num;
            } else if (num <= secondMin) {
                secondMin = num;
            } else {
                return true;
            }
        }
        return false;
    }
}
```

``` python
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        first = second = 2 ** 31 - 1
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
```
