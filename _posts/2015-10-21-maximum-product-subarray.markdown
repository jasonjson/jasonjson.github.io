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
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ret = min_val = max_val = nums[0]
        for i in range(1, len(nums)):
            min_val, max_val = min(min_val * nums[i], nums[i], max_val * nums[i]), max(min_val * nums[i], nums[i], max_val * nums[i])
            ret = max(ret, max_val)
        return ret
```
