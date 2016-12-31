---
layout: post
title: Sort Letters by Case
date: 2015-10-21 14:38:36.000000000 -04:00
type: post
published: true
status: publish
categories:
- Sorting
tags: []
meta:
  _wpas_done_all: '1'
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465803315;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1407;}i:1;a:1:{s:2:"id";i:87;}i:2;a:1:{s:2:"id";i:89;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a string which contains only letters. Sort it by lower case first and upper case second.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /** 
     *@param chars: The letter array you should sort by Case
     *@return: void
     */
    public void sortLetters(char[] chars) {
        //write your code here
        if (chars == null || chars.length == 0) return;
        
        int lo = 0, hi = chars.length - 1;
        while (lo <= hi) {
            while (lo <= hi && chars[lo] > 'Z') lo ++;
            while (lo <= hi && chars[hi] < 'a') hi --;
            if (lo <= hi) {
                swap(chars, lo, hi);
            }
        }
    }
    
    public void swap(char[] chars, int a, int b) {
        char temp = chars[a];
        chars[a] = chars[b];
        chars[b] = temp;
    }
}
</pre>
<p>[/expand]</p>
