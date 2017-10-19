---
layout: post
title: 238 - Product of Array Exclude Itself
date: 2015-10-21 02:19:40.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].**


``` java
public class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] left = new int[n];
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                left[i] = 1;
            } else {
                left[i] = left[i-1] * nums[i-1];
            }
        }

        int right = 1;
        for (int i = n - 1; i >= 0; i--) {
            if (i == n - 1) {
                right = 1;
            } else {
                right = right * nums[i+1];
            }
            left[i] = left[i] * right;
        }
        return left;
    }
}
```

``` python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums:
            return []
        ret = [1] * len(nums)
        for i in xrange(1, len(nums)):
            ret[i] = ret[i - 1] * nums[i - 1]
        right = 1
        for i in reversed(xrange(len(nums) - 1)):
            right = right * nums[i + 1]
            ret[i] *= right
        return ret
```
