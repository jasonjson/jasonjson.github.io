---
layout: post
title: Add Binary
date: 2015-10-21 01:34:39.000000000 -04:00
type: post
published: true
status: publish
categories:
- String
tags:
- Binary
- String
meta:
  _edit_last: '1'
  _spost_short_title: ''
  _wpcom_is_markdown: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463380879;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:900;}i:1;a:1:{s:2:"id";i:1267;}i:2;a:1:{s:2:"id";i:522;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong>Given two binary strings, return their sum (also a binary string).</strong></p>
<pre>public class Solution {
    /**
     * @param a a number
     * @param b a number
     * @return the result
     */
    public String addBinary(String a, String b) {
        // Write your code here
        int n = a.length(), m = b.length(), carry = 0;
        StringBuilder str = new StringBuilder();
        int i = n - 1, j = m - 1;
        while (carry != 0 || i >= 0 || j >= 0){
            if(i >= 0) {
                carry += Character.getNumericValue(a.charAt(i));
                i--;
            }
            if(j >= 0){
                carry += Character.getNumericValue(b.charAt(j));
                j--;
            }
            str.append(carry % 2);
            carry /= 2;
        }
        return str.reverse().toString();
    }
}
</pre>
