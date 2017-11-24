---
layout: post
title: 162 - Find Peak Element
date: 2015-10-21 02:28:54.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**A peak element is an element that is greater than its neighbors. Given an input array where num[i] !=  num[i+1], find a peak element and return its index. The array may contain multiple peaks, in that case return the index to any one of the peaks is fine. You may imagine that num[-1] = num[n] = -inf. For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.**


``` java
class Solution {
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    public int findPeak(int[] A) {
        // write your code here
        if (A == null) return -1;

        int lo = 0, hi = A.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (mid + 1 < A.length && A[mid] < A[mid + 1]) {
                lo = mid + 1;
            } else if (mid - 1 >= 0 && A[mid] < A[mid - 1]) {
                hi = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}
```

``` python
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if mid + 1 < len(nums) and nums[mid] < nums[mid + 1]:
                lo = mid + 1
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                hi = mid - 1
            else:
                return mid
        return -1
```
