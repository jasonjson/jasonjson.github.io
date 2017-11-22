---
layout: post
title: 397 - Longest Increasing Continuous subsequence
date: 2015-10-21 12:53:48.000000000 -04:00
tags:
- Lintcode
categories:
- Array
author: Jason
---
**Give you an integer array (index from 0 to n-1, where n is the size of this array)，find the longest increasing continuous subsequence in this array. (The definition of the longest increasing continuous subsequence here can be from right to left or from left to right)**


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

``` python
class Solution:
    """
    @param: A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        if not A:
            return 0
        ret = count = 1
        for i in xrange(1, len(A)):
            if A[i] > A[i - 1]:
                count += 1
            else:
                count = 1
            ret = max(ret, count)
        count = 1
        for i in reversed(xrange(len(A) - 1)):
            if A[i] > A[i + 1]:
                count += 1
            else:
                count = 1
            ret = max(ret, count)
        return ret
```
