---
layout: post
title: Sort Colors
date: 2015-10-21 14:37:34.000000000 -04:00
tags: algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue. Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.</em></strong></p>


``` java
public class Solution {
    public void sortColors(int[] nums) {
        if (nums == null || nums.length == 0) return;
        
        int left = 0, right = nums.length - 1;
        for (int i = left; i <= right; i++) {
            if (nums[i] == 0) {
                nums[i] = nums[left];
                nums[left++] = 0;
            } else if (nums[i] == 2) {
                nums[i] = nums[right];
                nums[right--] = 2;
                i--;
            }
        }
    }
}
```
