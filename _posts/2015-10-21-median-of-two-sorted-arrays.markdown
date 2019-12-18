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
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 0:
            return (self.helper(nums1, nums2, total_len // 2) + self.helper(nums1, nums2, total_len // 2 + 1)) / 2
        else:
            return self.helper(nums1, nums2, total_len // 2 + 1)

    def helper(self, nums1, nums2, k):
        if not nums1:
            return nums2[k - 1]
        if not nums2:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        index = k // 2 - 1
        m1 = nums1[index] if index < len(nums1) else 2 ** 31 - 1
        m2 = nums2[index] if index < len(nums2) else 2 ** 31 - 1
        if m1 < m2:
            return self.helper(nums1[index+1:], nums2, k - index - 1)
        else:
            return self.helper(nums1, nums2[index+1:], k - index - 1)
```
