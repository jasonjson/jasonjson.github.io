---
layout: post
title: Longest Consecutive Sequence
date: 2015-10-21 14:26:41.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
- Subarray
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1453264333;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:423;}i:1;a:1:{s:2:"id";i:331;}i:2;a:1:{s:2:"id";i:559;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an unsorted array of integers, find the length of the longest consecutive elements sequence.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param nums: A list of integers
     * @return an integer
     */
    public int longestConsecutive(int[] num) {
        // write you code here
        if (num == null || num.length == 0) return 0;
        int len = 0;
        Set<integer> set = new HashSet<integer>();
        for (int n : num) {
            set.add(n);
        }
        
        for (int n : num) {
            int left = n;
            while (set.remove(left)) {
                left--;
            }
            int right = n + 1;
            while (set.remove(right)) {
                right ++;
            }
            len = Math.max(len, right - left - 1);
        }
        return len;
    }
}
</integer></integer></pre>
<p>[/expand]</p>
