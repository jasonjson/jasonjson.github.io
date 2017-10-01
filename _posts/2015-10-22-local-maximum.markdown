---
layout: post
title: Local maximum
date: 2015-10-22 14:50:21.000000000 -04:00
tags:
- Leetcode
categories:
- Integer
author: Jason
---
<p><strong><em>Suppose we are given an array A[1···n] with the special property that A[1] ≤ A[2] and A[n − 1] >= A[n]. We say that an element A[i] is a local maximum if it is less than or equal to both its neighbors, or more formally, if A[i − 1] ≤ A[i] and A[i] ≥ A[i + 1]. For example, there are four local maximum in the following array: We can obviously find a</p>

local maximum in O(n) time by scanning through the array. Describe and analyze an algorithm that finds one local maximum in O(log n) time. (It is enough if your algorithm finds one local maximum. There is no need to find all local maxima.)</em></strong></p>
``` java
class Solution {
    public static int localMax(int[] nums) {
        if (nums == null || nums.length == 0) return 0;

        int lo = 1, hi = nums.length - 2;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] > nums[mid + 1] && nums[mid] > nums[mid - 1]) {
                return nums[mid];
            } else if (nums[mid] < nums[mid + 1]) {
                //two cases : nums[mid] > nums[mid - 1] or nums[mid] < nums[mid - 1]
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return -1;
    }
}
```
