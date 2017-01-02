---
layout: post
title: Wiggle Sort II
date: 2016-01-03 20:18:07.000000000 -05:00
categories:
- Sorting
author: Jason
---
<p><strong><em>Given an unsorted array nums, reorder it such that nums[0] &lt; nums[1] > nums[2] &lt; nums[3]....(wiggle sort I: nums[0] &lt;= nums[1] >= nums[2] &lt;= nums[3]...)</em></strong></p>


<p><a href="https://leetcode.com/discuss/77122/simple-modulo-solution">explanation</a></p>

``` java
public class Solution {
    public void wiggleSort(int[] nums) {
        if (nums == null || nums.length == 0) return;
        
        Arrays.sort(nums);
        int n = nums.length, mid = n % 2 == 0 ? n / 2 - 1 : n / 2;
        int[] temp = Arrays.copyOf(nums, n);
        int index = 0;
        for (int i = 0; i <= mid; i++) {
            nums[index] = temp[mid - i];
            if (index + 1 < n) {
                nums[index + 1] = temp[n - i - 1];
            }
            index += 2;
        }
    }
}
```
