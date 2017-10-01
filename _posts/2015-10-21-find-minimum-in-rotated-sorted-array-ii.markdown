---
layout: post
title: Find Minimum in Rotated Sorted Array II
date: 2015-10-21 02:30:37.000000000 -04:00
tags:
- Leetcode
categories:
- Integer
- Sorting
author: Jason
---
<p><strong><em>Suppose a sorted array is rotated at some pivot unknown to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2). Find the minimum element. The array may contain duplicates.</em></strong></p>


``` java
public class Solution {
    public int findMin(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] < nums[hi]) {
                hi = mid;
            } else if (nums[mid] > nums[hi]) {
                lo = mid + 1;
            } else {
                hi --;
            }
        }
        return nums[lo];
    }
}
```
