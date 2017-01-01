---
layout: post
title: String to Integer(atoi)
date: 2015-10-21 13:23:18.000000000 -04:00
type: post
published: true
status: publish
categories:
- String
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463405973;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:466;}i:1;a:1:{s:2:"id";i:87;}i:2;a:1:{s:2:"id";i:315;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Implement function atoi to convert a string to an integer. If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT&#95;MAX (2147483647) or INT&#95;MIN (-2147483648) is returned.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param str: A string
     * @return An integer
     */
    public int atoi(String str) {
        // write your code here
        if (str == null || str.length() == 0) return 0;
        
        str = str.trim();
        long result = 0;
        int index = 0, sign = 1;
        if (str.charAt(index) == '+') {
            index ++;
        } else if (str.charAt(index) == '-') {
            sign = -1;
            index ++;
        }
        for (; index < str.length(); index ++) {
            char c = str.charAt(index);
            if (!Character.isDigit(c)) {
                break;
            }
            result = result * 10 + sign * (c - '0');
            if (result >= Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            } else if (result <= Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }
        }
        return (int)result;
    }
}
</pre>
<p>[/expand]</p>
