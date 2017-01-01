---
layout: post
title: A + B Problem
date: 2015-10-21 02:39:12.000000000 -04:00
type: post
published: true
status: publish
categories:
- Bit
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1456382615;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:509;}i:1;a:1:{s:2:"id";i:36;}i:2;a:1:{s:2:"id";i:1073;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Write a function that add two numbers A and B. You should not use + or any arithmetic operators.</em></strong><br />
[expand title="code"]</p>
<pre>
class Solution {
    /*
     * param a: The first integer
     * param b: The second integer
     * return: The sum of a and b
     */
    public int aplusb(int a, int b) {
        // write your code here, try to do it without arithmetic operators.
        int result = a ^ b;
        int carry = a & b;
        carry <<= 1;
        if (carry != 0) {
            result = aplusb(result, carry);
        }
        return result;
    }
};
</pre>
<p>[/expand]</p>
