---
layout: post
title: 35 - Search Insert Position
date: 2015-10-21 02:27:15.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume NO duplicates in the array.**


``` java
public class Solution {
    /**
     * param A : an integer sorted array
     * param target :  an integer to be inserted
     * return : an integer
     */
    public int searchInsert(int[] A, int target) {
        if (A.length == 0) return 0;
        int lo = 0, hi = A.length - 1, mid = 0;
        while (lo <= hi){
            mid = (lo + hi) / 2;
            if (A[mid] == target) {
                return mid;
            }
            else if (A[mid] > target) {
                hi = mid - 1;
            }
            else {
                lo = mid + 1;
            }
        }
        return lo; //当循环停下来时，如果不是正好找到target，lo指向的元素恰好大于target，hi指向的元素恰好小于target，这里lo和hi可能越界，不过如果越界就说明大于（小于）target并且是最大（最小）
    }
}
```

``` python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
```
