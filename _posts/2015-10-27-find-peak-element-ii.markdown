---
layout: post
title: 163 - Find Peak Element II
date: 2015-10-27 11:15:26.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**There is an integer matrix which has the following features:
*. The numbers in adjacent positions are different.
*: The matrix has n rows and m columns.
*: For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].
*: For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].
**We define a position P is a peek if:**
* A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] && A[j][i] > A[j][i+1] && A[j][i] > A[j][i-1]
**Find a peak element in this matrix. Return the index of the peak.**

[Reference](http://courses.csail.mit.edu/6.006/spring11/lectures/lec02.pdf)


``` java
class Solution {
    /**
     * @param A: An integer matrix
     * @return: The index of the peak
     */
    public List<Integer> findPeakII(int[][] A) {
        // write your code here
        List<Integer> result = new ArrayList<Integer>();
        if (A == null || A.length == 0) return result;

        for (int i = 1; i < A.length - 1; i++) {//第一行和最后一行不用考虑
            int lo = 0, hi = A[0].length - 1;
            while (lo <= hi) {
                int mid = lo + (hi - lo) / 2;
                if (A[i][mid] < A[i][mid + 1]) {
                    lo = mid + 1;
                } else if (A[i][mid] < A[i][mid - 1]) {
                    hi = mid - 1;
                } else {
                    if (A[i][mid] > A[i - 1][mid] && A[i][mid] > A[i + 1][mid]) {
                        result.add(i);
                        result.add(mid);
                        return result;
                    }
                    break;
                }
            }
        }
        return result;
    }
}
```
