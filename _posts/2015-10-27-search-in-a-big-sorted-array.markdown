---
layout: post
title: Search in a Big Sorted Array
date: 2015-10-27 15:42:52.000000000 -04:00
type: post
published: true
status: publish
categories:
- Sorting
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467916334;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:145;}i:1;a:1:{s:2:"id";i:157;}i:2;a:1:{s:2:"id";i:149;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a big sorted array, find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number. Return -1, if the number doesn't exist in the array.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param A: An integer array
     * @param target: An integer
     * @return : An integer which is the index of the target number
     */
    public int searchBigSortedArray(int[] A, int target) {
        // write your code here
        if (A == null || A.length == 0) return -1;
        int lo = 0, hi = 0;
        while (hi < A.length && A[hi] < target) {
            hi = 2 * hi + 1;
        }
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (A[mid] == target) {
                while (mid - 1 >= 0 && A[mid - 1] == A[mid]) {
                    mid--;
                }
                return mid;
            } else if (A[mid] > target) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return -1;
    }
}
</pre>
<p>[/expand]</p>
