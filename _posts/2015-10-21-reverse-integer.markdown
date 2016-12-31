---
layout: post
title: Reverse Integer
date: 2015-10-21 03:28:44.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _inbound_impressions_count: '0'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465809712;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:505;}i:1;a:1:{s:2:"id";i:200;}i:2;a:1:{s:2:"id";i:1345;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Reverse digits of an integer.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param n the integer to be reversed
     * @return the reversed integer
     */
    public int reverseInteger(int n) {
        // Write your code here
        if (n > 0) return -reverseInteger(-n);
        
        long result = 0;
        while (n != 0) {
            result = result * 10 + n % 10;
            if (result < Integer.MIN_VALUE) {
                return 0;
            }
            n /= 10;
        }
        return (int) result;
    }
}
</pre>
<p>[/expand]</p>
