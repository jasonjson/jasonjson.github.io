---
layout: post
title: Wiggle Sort
date: 2015-10-29 14:09:31.000000000 -04:00
tags:
- Algorithm
categories:
- Sorting
author: Jason
---
<p><strong><em>Given an unsorted array nums, reorder it in-place such that nums[0] &lt;= nums[1] >= nums[2] &lt;= nums[3].... For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].</em></strong></p>


``` java
public class Solution {
    public void wiggleSort(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            if ((i % 2 == 1 && nums[i] < nums[i - 1]) || (i % 2 == 0 && nums[i] > nums[i - 1])) {
                //当i是基数, 必须大于左右两边,当i是偶数，必须小于左右两边
                int tmp = nums[i];
                nums[i] = nums[i - 1];
                nums[i - 1] = tmp;
            }
        }
    }
}
```
