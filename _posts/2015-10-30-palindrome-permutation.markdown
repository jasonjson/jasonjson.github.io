---
layout: post
title: Palindrome Permutation
date: 2015-10-30 15:34:35.000000000 -04:00
type: post
published: true
status: publish
categories:
- Palindrome
- Permutation
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469174876;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1208;}i:1;a:1:{s:2:"id";i:393;}i:2;a:1:{s:2:"id";i:1422;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a string, determine if a permutation of the string could form a palindrome.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public boolean canPermutePalindrome(String s) {
       if (s == null || s.length() == 0) return false;
       
       int[] count = new int[256];
       for (char c : s.toCharArray()) {
           if (count[c] > 0) {
               count[c] --;
           } else {
               count[c] ++; 
           }
       }
       int single = 0;
       for (int n : count) {
           if (n != 0) {
               single ++;
           }
           if (single > 1) {
               return false;
           }
       }
       return true;
    }
}
</pre>
<p>[/expand]</p>
