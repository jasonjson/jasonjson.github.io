---
layout: post
title: 300 - Longest Increasing Subsequence
date: 2015-10-21 12:53:11.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Given a sequence of integers, find the longest increasing subsequence (LIS). You code should return the length of the LIS.**
[reference](http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/)


``` java
public class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length, len = 1;
        int[] seq = new int[n];
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                seq[i] = nums[i];
            } else if (nums[i] <= seq[0]) {
                seq[0] = nums[i];
            } else if (nums[i] > seq[len - 1]) {
                seq[len++] = nums[i];
            } else {
                seq[findIndex(nums, 0, len - 1, nums[i])] = nums[i];
            }
        }
        return len;
    }

    public int findIndex(int[] nums, int lo, int hi, int key) {
    //find the index of first element in the array that is larger than key
        while (lo + 1 < hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] < key) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return hi;
    }
}
```

``` python
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        ret = []
        for i, num in enumerate(nums):
            index = self.find_index(ret, num)
            if index < len(ret):
                ret[index] = num
            else:
                ret.append(num)
        return len(ret)

    def find_index(self, nums, num):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid] < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
```
