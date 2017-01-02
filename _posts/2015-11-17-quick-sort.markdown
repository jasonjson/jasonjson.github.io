---
layout: post
title: Quick Sort
date: 2015-11-17 22:52:05.000000000 -05:00
categories:
- Sorting
author: Jason
---
<p><strong><em>Quick sort an integer array</em></strong></p>


``` java
public class Solution {
    public static void main(String[] args) {
        int[] nums = {2,12,3,46,1,2,4,5};
        quickSort(nums);
        for (int i : nums) {
            System.out.println(i);
        }
    }
    public static void quickSort(int[] nums) {
        if (nums == null || nums.length == 0) return;
        helper(nums, 0, nums.length - 1);
    }

    public static void helper(int[] nums, int start, int end) {
        if (start >= end) return;
        int index = partition(nums, start, end);
        helper(nums, start, index - 1);
        helper(nums, index + 1, end);
    }

    public static int partition(int[] nums, int start, int end) {
        int pivot = nums[start], index = start;
        for (int i = start + 1; i <= end; i++) {
            if (nums[i] <= pivot) {
                swap(nums, i, ++index);
            }
        }
        swap(nums, start, index);
        return index;
    }

    public static void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }

}
```
