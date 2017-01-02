---
layout: post
title: Median of unsorted array
date: 2015-10-21 02:25:36.000000000 -04:00
categories:
- Integer
author: Jason
---
<p><strong><em>Given a unsorted array with integers, find the median of it. A median is the middle number of the array after it is sorted. If there are even numbers in the array, return the N/2 th number after sorted.</em></strong></p>


``` java
public class Solution {
    /**
     * @param nums: A list of integers.
     * @return: An integer denotes the middle number of the array.
     */
    public int median(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return -1;
        
        return helper(nums, 0, nums.length - 1, (nums.length + 1) / 2);
    }
    
    public int helper(int[] nums, int start, int end, int k) {
        int lo = start, hi = end, pivot = end;
        while (lo <= hi) {
            while (lo <= hi && nums[lo] < nums[pivot]) lo ++;
            while (lo <= hi && nums[hi] >= nums[pivot]) hi --;
            if (lo < hi) {
                swap(nums, lo, hi);
            }
        }
        swap(nums, lo, pivot);
        if (lo + 1 == k) {
            return nums[lo];
        } else if (lo + 1 > k) {
            return helper(nums, start, lo - 1, k);
        } else {
            return helper(nums, lo + 1, end, k);
        }
    }
    
    public void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}
```
