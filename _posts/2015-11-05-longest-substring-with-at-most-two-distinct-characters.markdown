---
layout: post
title: Longest Substring with At Most Two Distinct Characters
date: 2015-11-05 16:22:23.000000000 -05:00
type: post
published: true
status: publish
categories:
- Two Pointers
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465620857;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1587;}i:1;a:1:{s:2:"id";i:1508;}i:2;a:1:{s:2:"id";i:545;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a string, find the length of the longest substring T that contains at most 2 distinct characters.<br />
For example, Given s = “eceba”,<br />
T is "ece" which its length is 3.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        if (s == null || s.length() == 0) return 0;
        
        int max = 1, start = 0, distinct = 0;
        int[] counts = new int[256];
        for (int i = 0; i < s.length(); i++) {
            if (counts[s.charAt(i)] == 0) {
                distinct++;
            }
            counts[s.charAt(i)]++;
            while (distinct > 2) {
                counts[s.charAt(start)] --;
                if (counts[s.charAt(start)] == 0) {
                    distinct --;
                }
                start ++;
            }
            max = Math.max(max, i - start + 1);
        }
        return max;
    }
}
</pre>
<p>[/expand]</p>
