---
layout: post
title: Digit Counts
date: 2015-10-21 14:03:43.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Integer
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467373045;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:200;}i:1;a:1:{s:2:"id";i:499;}i:2;a:1:{s:2:"id";i:991;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Count the number of k's between 0 and n. k can be 0 - 9.</em></strong></p>
<p>[expand title = "code1"]</p>
<pre>
class Solution {
    /*
     * param k : As description.
     * param n : As description.
     * return: An integer denote the count of digit k in 1..n
     */
    public int digitCounts(int k, int n) {
        if (k == 0 && n == 0) return 1;
        int result = 0, base = 1;
        while (n / base != 0) {
            if (k == 0 && base > 1) break; //k == 0, then 01 or 001 or 0001 are not numbers
            int hi = n / (base * 10);
            int curr = n / base % 10;
            int lo = n % base;
            if (curr > k) {
                result += (hi + 1) * base;
            } else if (curr == k) {
                result += hi * base + lo + 1;
            } else {
                result += hi * base;
            }
            base *= 10;
        }
        return result;
    }
};
</pre>
<p>[/expand]</p>
