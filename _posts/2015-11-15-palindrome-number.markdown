---
layout: post
title: Palindrome Number
date: 2015-11-15 17:33:12.000000000 -05:00
type: post
published: true
status: publish
categories:
- Integer
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466918992;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1227;}i:1;a:1:{s:2:"id";i:1489;}i:2;a:1:{s:2:"id";i:302;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Determine whether an integer is a palindrome. Do this without extra space.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        int temp = x, rev = 0;
        while (temp != 0) {
            rev = rev * 10 + temp % 10;
            temp /= 10;
        }
        return rev == x;
    }
}
</pre>
<p>[/expand]</p>
