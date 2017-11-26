---
layout: post
title: 330 - Patching Array
date: 2016-01-27 14:15:01.000000000 -05:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.**


``` java
//Let miss be the smallest sum in [1,n] that we might be missing. Meaning we already know we can build all sums in [1,miss). Then if we have a number num <= miss in the given array, we can add it to those smaller sums to build all sums in [1,miss+num). If we don't, then we must add such a number to the array, and it's best to add miss itself, to maximize the reach.
public class Solution {
    public int minPatches(int[] nums, int n) {
        long miss = 1;
        int result = 0, i = 0;
        while (miss <= n) {
            if (i < nums.length && nums[i] <= miss) {
                miss += nums[i++];
            } else {
                miss += miss;
                result ++;
            }
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """

        miss = 1
        ret = i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                ret += 1
        return ret
```
