---
layout: post
title: Search in Rotated Sorted Array II
date: 2015-10-21 02:29:40.000000000 -04:00
tags: algorithm
categories:
- Integer
- Sorting
author: Jason
---
<p><strong><em>Follow up for "Search in Rotated Sorted Array":</p>

What if duplicates are allowed? Would this affect the run-time complexity? How and why? Write a function to determine if a given target is in the array.</em></strong></p>

``` java
public class Solution {
    /** 
     * param A : an integer rotated sorted array and duplicates are allowed
     * param target :  an integer to be search
     * return : a boolean 
     */
    public boolean search(int[] A, int target) {
        // write your code here
        int len = A.length;
        if (A == null || len == 0) return false;
        
        int lo = 0, hi = len - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (A[mid] == target) return true;
            else if (A[lo] < A[mid]) {
                if (A[lo] <= target && target < A[mid]) {
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                } 
            }else if (A[lo] > A[mid]) {
                if (A[mid] < target && target <= A[hi]) {
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            // if A[start] == A[mid] we can only increment lo by 1 until we have found some element different from A[mid]
            } else {
                lo ++;
                // we can compare A[mid] with A[left] or A[right], both will work. However, if we compare with A[left] then we increment lo, if we compare with A[right], we decrement hi
            }
        }
        return false;
    }
}
```
