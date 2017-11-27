---
layout: post
title: 325 - Maximum Size Subarray Sum Equals k
date: 2016-01-05 12:18:15.000000000 -05:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.**


``` java
public class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        if (nums == null || nums.length == 0) return 0;

        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int sum = 0, len = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (sum == k) {
                len = Math.max(len, i + 1);
            } else if (map.containsKey(sum - k)) {
                len = Math.max(len, i - map.get(sum - k));
            }
            if (!map.containsKey(sum)) {
                map.put(sum, i);
            }
        }
        return len;
    }
}
```

``` python
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if not nums:
            return 0
        sum_map = {}
        summation = ret = 0
        for i, num in enumerate(nums):
            summation += num
            if summation == k:
                ret = max(ret, i + 1)
            elif summation - k in sum_map:
                ret = max(ret, i - sum_map[summation - k])
            #do not update if its in the map since we need the longest size
            if summation not in sum_map:
                sum_map[summation] = i
        return ret
```
