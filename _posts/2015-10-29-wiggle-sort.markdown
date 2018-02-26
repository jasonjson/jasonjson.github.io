---
layout: post
title: 280 - Wiggle Sort
date: 2015-10-29 14:09:31.000000000 -04:00
tags:
- Leetcode
categories:
- Sorting
author: Jason
---
**Given an unsorted array nums, reorder it in-place such that nums[0] &lt;= nums[1] >= nums[2] &lt;= nums[3].... For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].**


``` java
public class Solution {
    public void wiggleSort(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            if ((i % 2 == 1 && nums[i] < nums[i - 1]) || (i % 2 == 0 && nums[i] > nums[i - 1])) {
                int tmp = nums[i];
                nums[i] = nums[i - 1];
                nums[i - 1] = tmp;
            }
        }
    }
}
```

``` python
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        for i in xrange(1, len(nums)):
            if (i % 2 == 0 and nums[i] > nums[i - 1]) or (i % 2 != 0 and nums[i] < nums[i - 1]):
                nums[i], nums[i-1] = nums[i-1], nums[i]
```
