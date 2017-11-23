---
layout: post
title: 44 - Minimum Subarray
date: 2015-10-21 12:50:57.000000000 -04:00
tags:
- Lintcode
categories:
- Array
author: Jason
---
**Given an array of integers, find the subarray with smallest sum. Return the sum of the subarray.**


``` java
public class Solution {
    /**
     * @param nums: a list of integers
     * @return: A integer indicate the sum of minimum subarray
     */
    public int minSubArray(ArrayList<Integer> nums) {
        if (nums == null || nums.size() == 0) return 0;

        int min = Integer.MAX_VALUE, local = 0;
        for (int num : nums) {
            local = Math.min(local + num, num);
            min = Math.min(min, local);
        }
        return min;
    }
}
```

``` python
class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        if not nums:
            return 0

        ret = 2 ** 31 - 1
        summation = 0
        for num in nums:
            summation = min(summation + num, num)
            ret = min(ret, summation)
        return ret
```
