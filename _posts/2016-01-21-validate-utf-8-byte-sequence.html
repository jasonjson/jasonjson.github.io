---
layout: post
title: Validate UTF-8 byte sequence,
date: 2016-01-21 12:09:57.000000000 -05:00
type: post
published: true
status: publish
categories:
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466554782;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1054;}i:1;a:1:{s:2:"id";i:2075;}i:2;a:1:{s:2:"id";i:472;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em><a href="https://en.wikipedia.org/wiki/UTF-8#Description">Reference</a></em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public static boolean validate(byte[] bytes) {
        int expectedLen;
        if (bytes.length == 0) {
            return false;
        } else if ((bytes[0] & 0b10000000) == 0b00000000) {
            expectedLen = 1;
        } else if ((bytes[0] & 0b11100000) == 0b11000000) {
            expectedLen = 2;
        } else if ((bytes[0] & 0b11110000) == 0b11100000) {
            expectedLen = 3;
        } else if ((bytes[0] & 0b11111000) == 0b11110000) {
            expectedLen = 4;
        } else if ((bytes[0] & 0b11111100) == 0b11111000) {
            expectedLen = 5;
        } else if ((bytes[0] & 0b11111110) == 0b11111100) {
            expectedLen = 6;
        } else {
            return false;
        }
        if (expectedLen != bytes.length) {
            return false;
        }
        for (int i = 1; i < bytes.length; i++) {
            if ((bytes[i] & 0b11000000) != 0b10000000) {
                return false;
            }
        }
        return true;
    }
}
</pre>
<p>[/expand]</p>
