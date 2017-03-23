---
layout: post
title: Binary Search
date: 2015-10-21 02:26:49.000000000 -04:00
tags:
- Algorithm
categories:
- Integer
- Sorting
author: Jason
---
<p><strong><em>For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity. If the target number does not exist in the array, return -1.</em></strong></p>


``` java
class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        //write your code here
        int lo = 0, hi = nums.length - 1, index = -1;
        while (lo <= hi){
            int mid = (lo + hi) / 2;
            if(target == nums[mid]) {
                index = mid;
                break;
            } else if (target < nums[mid]) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        while(index > 0 && nums[index-1] == target) index--;
        return index;
    }
}
```
