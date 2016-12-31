---
layout: post
title: Excel Sheet Column Number
date: 2015-11-05 11:50:50.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467195101;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1359;}i:1;a:1:{s:2:"id";i:1357;}i:2;a:1:{s:2:"id";i:302;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a column title as appear in an Excel sheet, return its corresponding column number.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int titleToNumber(String s) {
        if (s == null || s.length() == 0) return 0;
        int result = 0;
        for (char c : s.toCharArray()) {
            result = result * 26 + (int)(c - 'A' + 1); 
        }
        return result;
    }
}
</pre>
<p>[/expand]</p>
