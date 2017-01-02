---
layout: post
title: Longest Increasing Continuous subsequence
date: 2015-10-21 12:53:48.000000000 -04:00
categories:
- Subarray
author: Jason
---
<p><strong><em>Give you an integer array (index from 0 to n-1, where n is the size of this array)，find the longest increasing continuous subsequence in this array. (The definition of the longest increasing continuous subsequence here can be from right to left or from left to right)</em></strong></p>

``` java
public class Solution {
    /**
     * @param A an array of Integer
     * @return  an integer
     */
    public int longestIncreasingContinuousSubsequence(int[] A) {
        if (A == null || A.length == 0) return 0;
        
        int maxLen = 1, count = 1;
        for (int i = 1; i < A.length; i++) {
            if (A[i] > A[i - 1]) {
                count ++;
            } else {
                count = 1;
            }
            maxLen = Math.max(maxLen, count);
        }
        count = 1;
        for (int i = A.length - 2; i >= 0; i--) {
            if (A[i] > A[i + 1]) {
                count ++;
            } else {
                count = 1;
            }
            maxLen = Math.max(maxLen, count);
        }
        return maxLen;
    }
}
```
