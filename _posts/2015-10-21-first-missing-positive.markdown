---
layout: post
title: First Missing Positive
date: 2015-10-21 02:20:34.000000000 -04:00
tags: algorithm
categories:
- Integer
author: Jason
---
<p><strong><em>Given an unsorted integer array, find the first missing positive integer.</em></strong></p>


``` java
public class Solution {
    public int firstMissingPositive(int[] nums) {
        if (nums == null || nums.length == 0) return 1;
        for (int i = 0; i < nums.length; i++) {
            while (nums[i] > 0 && nums[i] - 1 < nums.length && nums[nums[i] - 1] != nums[i]) {
                swap(nums, nums[i] - 1, i);//把一个positive int 放在应在在位置上
            //while loop, not if, we keep swapping
            }
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] - 1 != i) {
                return i + 1;
            }
        }
        return nums.length + 1;
    }
    public void swap(int[] nums, int a, int b) {
        int temp = nums[b];
        nums[b] = nums[a];
        nums[a] = temp;
    }
}
```
