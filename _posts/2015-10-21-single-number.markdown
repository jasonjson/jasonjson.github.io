---
layout: post
title: Single Number
date: 2015-10-21 02:33:24.000000000 -04:00
type: post
published: true
status: publish
categories:
- Bit
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466265795;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:499;}i:1;a:1:{s:2:"id";i:536;}i:2;a:1:{s:2:"id";i:200;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given 2n + 1 numbers, every numbers occurs twice except one, find it.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     *@param A : an integer array
     *return : a integer 
     */
    public int singleNumber(int[] A) {
        int result = 0;
        for (int n : A) {
            result ^= n;
        }
        return result;
    }
}
</pre>
<p>[/expand]</p>
