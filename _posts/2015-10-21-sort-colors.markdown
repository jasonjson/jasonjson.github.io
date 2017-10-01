---
layout: post
title: Sort Colors
date: 2015-10-21 14:37:34.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue. Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.**


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

``` python
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        index, left, right = 0, 0, len(nums) - 1
        while index >= left and index <= right:
            if nums[index] == 0:
                nums[index] = nums[left]
                nums[left] = 0
                left += 1
            elif nums[index] == 2:
                nums[index] = nums[right]
                nums[right] = 2
                right -= 1
                index -= 1 #nums[right]换过来后还没有比较
            index += 1
```
