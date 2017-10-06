---
layout: post
title: 152 - Maximum Product Subarray
date: 2015-10-21 14:30:37.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Find the contiguous subarray within an array (containing at least one number) which has the largest product.**


``` java
public class Solution {
    public int maxProduct(int[] nums) {
        if (nums == null || nums.length == 0) return -1;
        int min = 1, max = 1, global = Integer.MIN_VALUE;
        for (int n : nums) {
            int temp = max;
            max = Math.max(max * n, Math.max(min * n, n));
            min = Math.min(temp * n, Math.min(min * n, n));
            global = Math.max(max, global);
        }
        return global;
    }
}
```

``` python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        min_product = max_product = 1
        ret = nums[0]
        for num in nums:
            tmp = max_product
            max_product = max(max_product * num, min_product * num, num)
            min_product = min(tmp * num, min_product * num, num)
            ret = max(ret, max_product)
        return ret
```
