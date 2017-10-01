---
layout: post
title: Move Zeroes
date: 2015-10-28 13:19:18.000000000 -04:00
tags:
- Leetcode
categories:
- Integer
- Two Pointers
author: Jason
---
<p><strong><em>Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements. For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0]. Note: You must do this in-place without making a copy of the array. Minimize the total number of operations.</em></strong></p>


``` java
public class Solution {
    public void moveZeroes(int[] nums) {
        if (nums == null || nums.length == 0) return;
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                int temp = nums[index];
                nums[index++] = nums[i];
                nums[i] = temp;
            }
        }
    }
}
```

``` java
public class Solution {
    public void moveZeroes(int[] nums) {
        if (nums == null || nums.length == 0) return;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                int j = i + 1;
                while (j < nums.length) {
                    if (nums[j] != 0) {
                        break;
                    } else {
                        j ++;
                    }
                }
                if (j < nums.length) {
                    swap(nums, i, j);
                }
            }
        }
    }
    
    public void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}
```
