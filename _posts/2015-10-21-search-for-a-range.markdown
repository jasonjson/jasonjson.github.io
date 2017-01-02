---
layout: post
title: Search for a Range
date: 2015-10-21 02:27:43.000000000 -04:00
categories:
- Integer
- Sorting
author: Jason
---
<p><strong><em>Given a sorted array of integers, find the starting and ending position of a given target value. Your algorithm's runtime complexity must be in the order of O(log n). If the target is not found in the array, return [-1, -1].</em></strong></p>


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
