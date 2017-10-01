---
layout: post
title: Product of Array Exclude Itself
date: 2015-10-21 02:19:40.000000000 -04:00
tags:
- Leetcode
categories:
- Integer
author: Jason
---
<p><strong><em>Given an integers array A. Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1], calculate B WITHOUT divide operation.</em></strong></p>


``` java
public class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] left = new int[n];
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                left[i] = 1;
            } else {
                left[i] = left[i-1] * nums[i-1];
            }
        }
        
        int right = 1;
        for (int i = n - 1; i >= 0; i--) {
            if (i == n - 1) {
                right = 1;
            } else {
                right = right * nums[i+1];
            }
            left[i] = left[i] * right;
        }
        return left;
    }
}
```
