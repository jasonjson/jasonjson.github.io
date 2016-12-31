---
layout: post
title: Happy Number
date: 2015-11-04 15:15:26.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1455596103;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1227;}i:1;a:1:{s:2:"id";i:1424;}i:2;a:1:{s:2:"id";i:107;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Write an algorithm to determine if a number is "happy".<br />
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public boolean isHappy(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10; 
            sum += digit * digit;
            n /= 10;
        }
        if (sum > 9) { 
            return (isHappy(sum));
        } else {
            return sum == 1;
        }
    }
}
</pre>
<p>[/expand]</p>
