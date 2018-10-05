---
layout: post
title: 34 - Search for a Range
date: 2015-10-21 02:27:43.000000000 -04:00
tags:
- Leetcode
categories:
- Sorting
author: Jason
---
**Given a sorted array of integers, find the starting and ending position of a given target value. Your algorithm's runtime complexity must be in the order of O(log n). If the target is not found in the array, return [-1, -1].**


``` java
public class Solution {
    /**
     *@param A : an integer sorted array
     *@param target :  an integer to be inserted
     *return : a list of length 2, [index1, index2]
     */
    public int[] searchRange(int[] A, int target) {
        // write your code here
        int[] result = new int[] {-1, -1};
        if (A == null || A.length == 0) {
            return result;
        }

        int lo = 0, hi = A.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (A[mid] == target) {
                int left = mid, right = mid;
                while (left - 1 >= lo && A[left - 1] == target) {
                    left --;
                }
                while (right + 1 <= hi && A[right + 1] == target) {
                    right ++;
                }
                result[0] = left;
                result[1] = right;
                break;
            } else if (A[mid] > target) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if not nums or target is None:
            return [-1, -1]

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid] == target:
                left, right = mid - 1, mid + 1
                while left >= 0 and nums[left] == target:
                    left -= 1
                while right < len(nums) and nums[right] == target:
                    right += 1
                return [left + 1, right - 1]
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return [-1, -1]
```