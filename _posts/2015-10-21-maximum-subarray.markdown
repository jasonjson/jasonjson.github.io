---
layout: post
title: Maximum Subarray
date: 2015-10-21 12:50:20.000000000 -04:00
tags:
- Algorithm
categories:
- Dynamic Programming
author: Jason
---
**Given an array of integers, find a contiguous subarray which has the largest sum.**


``` java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A integer indicate the sum of max subarray
     */
    public int maxSubArray(ArrayList<integer> nums) {
        if (nums == null || nums.size() == 0) return 0;

        int local = 0, max = Integer.MIN_VALUE;
        for (int num : nums) {
            local = Math.max(local + num, num);//num must be the last number in local
            max = Math.max(max, local);
        }
        return max;
    }
}
```

``` python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        local, ret = 0, -2**31
        for num in nums:
            local = max(num, local + num)
            ret = max(ret, local)
        return ret
```
