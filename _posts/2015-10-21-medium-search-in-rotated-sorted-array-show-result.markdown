---
layout: post
title: Search in rotated sorted array
date: 2015-10-21 02:29:17.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
- Sorting
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465790492;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:159;}i:1;a:1:{s:2:"id";i:163;}i:2;a:1:{s:2:"id";i:161;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Suppose a sorted array is rotated at some pivot unknown to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2). You are given a target value to search. If found in the array return its index, otherwise return -1. You may assume no duplicate exists in the array.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /** 
     *@param A : an integer rotated sorted array
     *@param target :  an integer to be searched
     *return : an integer
     */
    public int search(int[] A, int target) {
        // write your code here
        int len = A.length;
        //error check
        if (A == null || len == 0) return -1;
        
        int lo = 0, hi = len - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (A[mid] == target) return mid;
            else if (A[mid] > A[hi]) {
            //left half is ordered
                if (A[lo] <= target && target < A[mid]) {
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                } 
            } else { //right half is ordered
                if (A[mid] < target && target <= A[hi]) {
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
        }
        return -1;
    }
}
</pre>
<p>[/expand]</p>
