---
layout: post
title: Shortest Palindrome
date: 2015-11-03 17:45:22.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468903918;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1422;}i:1;a:1:{s:2:"id";i:393;}i:2;a:1:{s:2:"id";i:307;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
//The key point is to find the longest palindrome starting from the first character, and then reverse the remaining part as the prefix to s.
    public String shortestPalindrome(String s) {
        int i = 0, end = s.length() - 1, j = end;
        while (i < j) {
             if (s.charAt(i) == s.charAt(j)) {
                 i++; 
                 j--;
             } else { 
                 i = 0; //重新开始,必须从第一个字母开始找
                 end--; //关键是找到end,是包括首字母的最长的palindrome
                 j = end;
             }
        }
        return new StringBuilder(s.substring(end+1)).reverse().toString() + s;
    }
}
</pre>
<p>[/expand]</p>
