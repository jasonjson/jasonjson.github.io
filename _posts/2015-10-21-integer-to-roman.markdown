---
layout: post
title: Integer to Roman
date: 2015-10-21 14:20:00.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467900197;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1359;}i:1;a:1:{s:2:"id";i:503;}i:2;a:1:{s:2:"id";i:1489;}}}}
  _wpas_done_all: '1'
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an integer, convert it to a roman numeral. The number is guaranteed to be within the range from 1 to 3999.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public String intToRoman(int n) {
        StringBuilder result = new StringBuilder();
        int scale = 1000;
        String[] roman = {"I","V","X","L","C","D","M"};
        for (int i = 6; i >= 0; i -= 2) {
            int digit = n / scale;
            if (digit <= 3) {
                for (int j = 0; j < digit; j++) {
                    result.append(roman[i]);
                }
            } else if (digit == 4) {
                result.append(roman[i]).append(roman[i+1]);
            } else if (digit == 5) {
                result.append(roman[i+1]);
            } else if (digit <= 8) {
                result.append(roman[i+1]);
                for (int j = 0; j < digit - 5; j++) {
                    result.append(roman[i]);
                }
            } else if (digit == 9) {
                result.append(roman[i]).append(roman[i+2]);
            }
            n %= scale;
            scale /= 10;
        }
        return result.toString();
    }
}
</pre>
<p>[/expand]</p>
