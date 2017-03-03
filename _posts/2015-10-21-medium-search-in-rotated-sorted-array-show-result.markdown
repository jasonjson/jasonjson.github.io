---
layout: post
title: Search in rotated sorted array
date: 2015-10-21 02:29:17.000000000 -04:00
tags: algorithm
categories:
- Integer
- Sorting
author: Jason
---
<p><strong><em>Suppose a sorted array is rotated at some pivot unknown to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2). You are given a target value to search. If found in the array return its index, otherwise return -1. You may assume no duplicate exists in the array.</em></strong></p>


``` java
public class Solution {
    /** 
     *@param A : an integer rotated sorted array
     *@param target :  an integer to be searched
     *return : an integer
     */
    public int search(int[] A, int target) {
        // write your code here
        int len = A.length;
        //error check
        if (A == null || len == 0) return -1;
        
        int lo = 0, hi = len - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (A[mid] == target) return mid;
            else if (A[mid] > A[hi]) {
            //left half is ordered
                if (A[lo] <= target && target < A[mid]) {
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                } 
            } else { //right half is ordered
                if (A[mid] < target && target <= A[hi]) {
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
        }
        return -1;
    }
}
```
