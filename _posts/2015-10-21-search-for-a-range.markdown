---
layout: post
title: Search for a Range
date: 2015-10-21 02:27:43.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
- Sorting
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465970988;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1087;}i:1;a:1:{s:2:"id";i:157;}i:2;a:1:{s:2:"id";i:159;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a sorted array of integers, find the starting and ending position of a given target value. Your algorithm's runtime complexity must be in the order of O(log n). If the target is not found in the array, return [-1, -1].</em></strong><br />
[expand title="code"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
