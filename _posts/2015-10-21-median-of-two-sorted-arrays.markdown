---
layout: post
title: Median of Two Sorted Arrays
date: 2015-10-21 02:31:58.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
- Sorting
- Subarray
tags:
- Hard
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465444142;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:139;}i:1;a:1:{s:2:"id";i:294;}i:2;a:1:{s:2:"id";i:1038;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).</em></strong><br />
[expand title="code"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
