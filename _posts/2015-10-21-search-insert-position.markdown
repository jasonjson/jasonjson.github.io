---
layout: post
title: Search Insert Position
date: 2015-10-21 02:27:15.000000000 -04:00
tags: algorithm
categories:
- Binary Search Tree
- Sorting
author: Jason
---
<p><strong><em>Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume NO duplicates in the array.</em></strong></p>


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
        //cases where target is not present in the array
        return lo; //当循环停下来时，如果不是正好找到target，lo指向的元素恰好大于target，hi指向的元素恰好小于target，这里lo和hi可能越界，不过如果越界就说明大于（小于）target并且是最大（最小）
    }
}
```
