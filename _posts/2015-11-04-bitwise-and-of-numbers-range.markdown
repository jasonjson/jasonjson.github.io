---
layout: post
title: Bitwise AND of Numbers Range
date: 2015-11-04 15:36:13.000000000 -05:00
type: post
published: true
status: publish
categories:
- Bit
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467019407;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1258;}i:1;a:1:{s:2:"id";i:1373;}i:2;a:1:{s:2:"id";i:522;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a range [m, n] where 0 &lt;= m &lt;= n &lt;= 2147483647, return the bitwise AND of all numbers in this range, inclusive.<br />
For example, given the range [5, 7], you should return 4.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        int diffDigits = 0;
        while (m != n) {
            m >>= 1;
            n >>= 1;
            diffDigits ++;
        }
        return n << diffDigits;
    }//Find the same prefix of the numbers in this range.
}
</pre>
<p>[/expand]</p>
