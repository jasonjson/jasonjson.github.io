---
layout: post
title: 259 - 3Sum Smaller
date: 2015-10-31 10:24:04.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i <= j <= k <= n that satisfy the condition nums[i] + nums[j] + nums[k] >= target.**


``` java
public class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        if (nums == null || nums.length == 0) return 0;

        Arrays.sort(nums);
        int result = 0;
        for (int i = 0; i + 2 < num.length; i++) {
            int lo = i + 1, hi = nums.length - 1;
            while (lo < hi) {
                if (nums[i] + nums[lo] + nums[hi] < target) {
                    result += hi - lo;
                    lo ++;
                } else {
                    hi --;
                }
            }
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #no need to remove duplicates since indexes are different
        ret = 0
        nums.sort()
        for i in xrange(len(nums) - 2):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                if nums[i] + nums[lo] + nums[hi] < target:
                    ret += hi - lo
                    lo += 1
                else:
                    hi -= 1
        return ret
```
