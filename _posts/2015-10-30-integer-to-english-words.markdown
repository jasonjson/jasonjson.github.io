---
layout: post
title: Integer to English Words
date: 2015-10-30 10:40:37.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Integer
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465267081;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:505;}i:1;a:1:{s:2:"id";i:1201;}i:2;a:1:{s:2:"id";i:1227;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public String numberToWords(int num) {
        if (num == 0) return "Zero";
        StringBuilder sb = new StringBuilder();
        String[] ones = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        String[] teens = {"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
        String[] tens = {"Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
        int base = 0;
        while (num > 0) {
            int curr = num % 1000;
            num /= 1000;
            if (base == 1 && curr > 0) sb.insert(0, "Thousand ");
            if (base == 2 && curr > 0) sb.insert(0, "Million ");
            if (base == 3 && curr > 0) sb.insert(0, "Billion ");
            int one = curr % 10; curr /= 10;
            int teen = curr % 10; curr /= 10;
            int hundred = curr % 10;
            if (teen == 1) {
                sb.insert(0, teens[one] + " ");
            } else {
                if (one > 0) sb.insert(0, ones[one] + " ");
                if (teen > 0) sb.insert(0, tens[teen] + " ");
            }
            if (hundred > 0) sb.insert(0, ones[hundred] + " Hundred ");
            base ++;
        }
        return sb.toString().trim();//trim() is for the case 23 not "twenty three " but "twenty three", the space after three
    }
}
</pre>
<p>[/expand]</p>
