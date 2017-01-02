---
layout: post
title: Range Sum Query - Immutable
date: 2015-11-10 09:14:36.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.</em></strong></p>

``` java
public class NumArray {
    int[] sums;
    public NumArray(int[] nums) {
        sums = new int[nums.length + 1];
        for (int i = 1; i <= nums.length; i++) {
            sums[i] = sums[i - 1] + nums[i - 1];
        }
    }

    public int sumRange(int i, int j) {
        return sums[j + 1] - sums[i];
    }
}
```
