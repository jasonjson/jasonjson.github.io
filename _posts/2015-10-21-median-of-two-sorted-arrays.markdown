---
layout: post
title: 4 - Median of Two Sorted Arrays
date: 2015-10-21 02:31:58.000000000 -04:00
tags:
- Leetcode
categories:
- Sorting
author: Jason
---
**There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).**

``` java
class Solution {
    /**
     * @param A: An integer array.
     * @param B: An integer array.
     * @return: a double whose format is *.5 or *.0
     */
    public double findMedianSortedArrays(int[] A, int[] B) {
        // write your code here
        int len = A.length + B.length;
        if (len % 2 == 0) {
            return (helper(A, 0, B, 0, len / 2) + helper(A, 0, B, 0, len / 2 + 1)) / 2.0;
        } else {
            return helper(A, 0, B, 0, len / 2 + 1);
        }
    }

    public double helper(int[] A, int A_start, int[] B, int B_start, int k) {
        if (A_start >= A.length) {
            return B[B_start + k - 1];
        }
        if (B_start >= B.length) {
            return A[A_start + k - 1];
        }
        if (k == 1) {
            return Math.min(A[A_start], B[B_start]);
        }
        int key1 = A_start + k / 2 - 1 < A.length ? A[A_start + k / 2 - 1] : Integer.MAX_VALUE;
        int key2 = B_start + k / 2 - 1 < B.length ? B[B_start + k / 2 - 1] : Integer.MAX_VALUE;
        if (key1 < key2) {//A_start not 0 !!!
            return helper(A, A_start + k / 2, B, B_start, k - k / 2);
        } else {
            return helper(A, A_start, B, B_start + k / 2, k - k / 2);
        }
    }
}
```

``` python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_length = len(nums1) + len(nums2)
        if total_length % 2 == 0:
            return (self.helper(nums1, 0, nums2, 0, total_length / 2) + self.helper(nums1, 0, nums2, 0, total_length / 2 + 1)) / 2.0
        else:
            return self.helper(nums1, 0, nums2, 0, total_length / 2 + 1)

    def helper(self, a, a_start, b, b_start, k):
        if a_start >= len(a):
            return b[b_start + k - 1]
        elif b_start >= len(b):
            return a[a_start + k - 1]
        elif k == 1:
            return min(a[a_start], b[b_start])
        else:
            k1 = a[a_start + k / 2 - 1] if a_start + k / 2 - 1 < len(a) else 2 ** 31
            k2 = b[b_start + k / 2 - 1] if b_start + k / 2 - 1 < len(b) else 2 ** 31
            if k1 < k2:
                return self.helper(a, a_start + k / 2, b, b_start, k - k / 2)
            else:
                return self.helper(a, a_start, b, b_start + k / 2, k - k / 2)
```
