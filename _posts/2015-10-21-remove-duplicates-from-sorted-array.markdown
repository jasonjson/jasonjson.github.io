---
layout: post
title: 26 - Remove Duplicates from Sorted Array
date: 2015-10-21 02:23:37.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length. Do not allocate extra space for another array, you must do this in place with constant memory. For example, Given input array nums = [1,1,2], Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.**


``` java
public class Solution {
    /**
     * @param A: a array of integers
     * @return : return an integer
     */
    public int removeDuplicates(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return 0;
        int index = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i-1]) {
                index ++;
            }
            nums[index] = nums[i];
        }
        return index + 1;//长度比index多1
    }
}
```

``` python
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        index = 0
        for i, num in enumerate(nums[1:])
            if num != nums[i - 1]:
                index += 1
                nums[index] = num

        return index + 1
```
