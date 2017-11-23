---
layout: post
title: 31 - Partition Array
date: 2015-10-21 02:20:04.000000000 -04:00
tags:
- Lintcode
categories:
- Array
author: Jason
---
**Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that: All elements &lt; k are moved to the leff. All elements >= k are moved to the right Return the partitioning index, i.e the first index i nums[i] >= k.**


``` java
public class Solution {
    /**
     *@param nums: The integer array you should partition
     *@param k: As description
     *return: The index after partition
     */
    public int partitionArray(int[] nums, int k) {
        //write your code here
        int i = 0, j = nums.length - 1;
        while (i <= j) {
            while (i <= j && nums[i] < k) i++;
            while (i <= j && nums[j] >= k) j--;
            if (i < j) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
                j--;
            }
        }
        return i;
    }
}
```

``` python
class Solution:
    """
    @param: nums: The integer array you should partition
    @param: k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if not nums:
            return 0
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            if nums[lo] < k:
                lo += 1
                continue
            if nums[hi] >= k:
                hi -= 1
                continue
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1
        return lo
```
