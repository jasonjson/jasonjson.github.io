---
layout: post
title: 16 - 3Sum Closest
date: 2015-10-21 02:22:25.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.**


``` java
public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        if (nums == null || nums.length < 3) return -1;

        Arrays.sort(nums);
        int n = nums.length;
        int result = nums[0] + nums[1] + nums[2];
        for (int i = 0; i + 2 < n; i++) {
            int lo = i + 1, hi = n - 1;
            while (lo < hi) {
                int sum = nums[i] + nums[lo] + nums[hi];
                if (sum == target) {
                    return target;
                } else if (sum < target) {
                    lo++;
                } else {
                    hi--;
                }
                if (Math.abs(result - target) > Math.abs(sum - target)) {
                    result = sum;
                }
            }
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return 0

        ret = sum(nums[:3])
        nums.sort()
        for i, num in enumerate(nums[:-2]):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                total = num + nums[lo] + nums[hi]
                if total == target:
                    return total
                elif total > target:
                    hi -= 1
                else:
                    lo += 1
                if abs(total - target) < abs(ret - target):
                    ret = total
        return ret
```
