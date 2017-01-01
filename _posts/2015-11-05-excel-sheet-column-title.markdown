---
layout: post
title: Excel Sheet Column Title
date: 2015-11-05 11:43:27.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466209995;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:343;}i:1;a:1:{s:2:"id";i:1365;}i:2;a:1:{s:2:"id";i:539;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a positive integer, return its corresponding column title as appear in an Excel sheet.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public String convertToTitle(int n) {
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            int digit = n % 26;
            n /= 26;
            if (digit == 0) {//deal with 26 separately
                sb.append("Z");
                n --;
            } else {
                sb.append((char)(digit - 1 + 'A'));
            }
        }
        return sb.reverse().toString();
    }
}
</pre>
<p>[/expand]</p>
