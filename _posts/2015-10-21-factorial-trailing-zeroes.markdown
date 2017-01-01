---
layout: post
title: Factorial Trailing Zeroes
date: 2015-10-21 02:36:12.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467200569;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1333;}i:1;a:1:{s:2:"id";i:1258;}i:2;a:1:{s:2:"id";i:1919;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an integer n, return the number of trailing zeroes in n!. Note: Your solution should be in logarithmic time complexity.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
//to compute the number of trailing zeros, we need to first think clear about what will generate a trailing 0? Obviously, a number multiplied by 10 will have a trailing 0 added to it. So we only need to find out how many 10's will appear in the expression of the factorial. Since 10 = 2 * 5 and there are a bunch more 2's (each even number will contribute at least one 2), we only need to count the number of 5's.
    public int trailingZeroes(int n) {
        int count = 0;
        if (n < 0) return -1;
        while (n > 0) {
            count += n / 5;
            n = n / 5;
        }
        return count;
    }
    //recursive
    public int trailingZeroes(int n) {
        if (n < 0) return -1;
        if (n == 0) return 0;
        return n / 5 + trailingZeroes(n / 5);
    }
}
</pre>
<p>[/expand]</p>
