---
layout: post
title: Unique Characters
date: 2015-10-21 03:35:07.000000000 -04:00
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
  _series_part: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465289292;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:471;}i:1;a:1:{s:2:"id";i:612;}i:2;a:1:{s:2:"id";i:1152;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Implement an algorithm to determine if a string has all unique characters.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param str: a string
     * @return: a boolean
     */
    public boolean isUnique(String str) {
        // write your code here
        if (str == null || str.length() == 0) return false;
        int[] existed = new int[256];
        
        for (int i = 0; i < str.length(); i++) {
            if (++existed[str.charAt(i)] > 1) return false;
        }
        return true;
    }
    //no extra space
    public boolean isUnique(String str) {
        // write your code here
        if (str == null || str.length() == 0) return false;
        
        for (int i = 0; i < str.length(); i++) {
            for (int j = i + 1; j < str.length(); j++) {
                if (str.charAt(i) == str.charAt(j)) {
                    return false;
                }
            }
        }
        return true;
    }
}
</pre>
<p>[/expand]</p>
