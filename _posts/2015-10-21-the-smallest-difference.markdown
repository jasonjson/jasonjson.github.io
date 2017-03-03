---
layout: post
title: The Smallest Difference
date: 2015-10-21 14:39:14.000000000 -04:00
tags: algorithm
categories:
- Integer
- Sorting
author: Jason
---
<p><strong><em>Given two array of integers(the first array is array A, the second array is array B), now we are going to find a element in array A which is A[i], and another element in array B which is B[j], so that the difference between A[i] and B[j] (|A[i] - B[j]|) is as small as possible, return their smallest difference.</em></strong></p>


``` java
public class Solution {
    /**
     * @param A, B: Two integer arrays.
     * @return: Their smallest difference.
     */
    public int smallestDifference(int[] A, int[] B) {
        Arrays.sort(A);
        Arrays.sort(B);
        int i = 0, j = 0, diff = Integer.MAX_VALUE;
        while (i < A.length && j < B.length) {
            diff = Math.min(diff, Math.abs(A[i] - B[j]));
            if (A[i] < B[j]) {
                i ++;
            } else {
                j ++;
            }
        }
        return diff;
    }
}

```
