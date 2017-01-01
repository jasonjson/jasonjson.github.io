---
layout: post
title: Compare Strings
date: 2015-10-21 02:11:25.000000000 -04:00
type: post
published: true
status: publish
categories:
- String
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463968537;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:577;}i:1;a:1:{s:2:"id";i:1357;}i:2;a:1:{s:2:"id";i:1320;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Compare two strings A and B, determine whether A contains all of the characters in B. The characters in string A and B are all Upper Case letters.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param A : A string includes Upper Case letters
     * @param B : A string includes Upper Case letter
     * @return :  if string A contains all of the characters in B return true else return false
     */
    public boolean compareStrings(String A, String B) {
        // write your code here
        if (B.length() == 0) return true;//error check !!!
        if (A.length() == 0) return false;
        
        int[] letters = new int[26];
        for (char c : A.toCharArray()) {
            letters[c - 'A'] ++;
        }
        for (char c : B.toCharArray()) {
            if (--letters[c - 'A'] < 0) {
                return false;
            }
        }
        return true;
    }   
</pre>
<p>[/expand]</p>
