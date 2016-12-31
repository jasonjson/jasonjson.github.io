---
layout: post
title: Binary Representation
date: 2015-10-22 08:28:06.000000000 -04:00
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
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465725037;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:36;}i:1;a:1:{s:2:"id";i:522;}i:2;a:1:{s:2:"id";i:1267;}}}}
  _inbound_impressions_count: '0'
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a (decimal - e.g. 3.72) number that is passed in as a string, return the binary representation that is passed in as a string. If the fractional part of the number can not be represented accurately in binary with at most 32 characters, return ERROR.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public String binaryRepresentation(String n) {
        if (n == null || n.length() == 0) return "";
        
        StringBuilder left_binary = new StringBuilder(), right_binary = new StringBuilder();
        int i = 0;
        for (; i < n.length(); i++) {
            if (n.charAt(i) == '.') {
                break;
            }
        }
        int left = Integer.parseInt(n.substring(0, i));
        double right = Double.parseDouble(n.substring(i));
        while (left > 0) {
            left_binary.append(left % 2);
            left /= 2;
        }
        while (right > 0) {
            right *= 2;
            if (right >= 1) {
                right_binary.append(1);
                right -= 1;
            } else {
                right_binary.append(0);
            }
        }//key: corner cases
        if (right_binary.length() >= 32) {
            return "ERROR";
        } else if (right_binary.length() == 0 && left_binary.length() == 0) {
            return "0"; //input 0.0
        } else if (right_binary.length() == 0) {//input 1.0 output 1 not 1.0
            return left_binary.reverse().toString();
        } else if (left_binary.length() == 0) {//input 0.5 output 0.1 not .1
            return "0." + right_binary;
        } else {
            return left_binary.reverse().toString() + "." + right_binary;
        }
    }
}
</pre>
<p>[/expand]</p>
