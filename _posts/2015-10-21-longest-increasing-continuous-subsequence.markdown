---
layout: post
title: Longest Increasing Continuous subsequence
date: 2015-10-21 12:53:48.000000000 -04:00
type: post
published: true
status: publish
categories:
- Subarray
tags: []
meta:
  _spost_short_title: ''
  _wpas_done_all: '1'
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466477544;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:423;}i:1;a:1:{s:2:"id";i:426;}i:2;a:1:{s:2:"id";i:75;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Give you an integer array (index from 0 to n-1, where n is the size of this array)，find the longest increasing continuous subsequence in this array. (The definition of the longest increasing continuous subsequence here can be from right to left or from left to right)</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
