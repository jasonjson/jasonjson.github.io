---
layout: post
title: Longest Substring with At Most K Distinct Characters
date: 2015-11-19 18:10:55.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Two Pointers
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468116418;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:545;}i:1;a:1:{s:2:"id";i:1382;}i:2;a:1:{s:2:"id";i:93;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a string s, find the length of the longest substring T that contains at most k distinct characters.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param s : A string
     * @return : The length of the longest substring 
     *           that contains at most k distinct characters.
     */
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        // write your code here
        if (s == null || s.length() == 0) return 0;
        
        int start = 0, maxLen = 0, distinct = 0;
        int[] letter = new int[256];
        for (int i = 0; i < s.length(); i++) {
            letter[s.charAt(i)] ++;
            if (letter[s.charAt(i)] == 1) {
                distinct ++;
            }
            while (distinct > k) {
                if (--letter[s.charAt(start++)] == 0) {
                    distinct --;
                }
            }
            maxLen = Math.max(maxLen, i - start + 1);
        }
        return maxLen;
    }
}
</pre>
<p>[/expand]</p>
