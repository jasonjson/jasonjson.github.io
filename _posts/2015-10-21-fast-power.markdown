---
layout: post
title: Fast Power
date: 2015-10-21 02:37:36.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468874040;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1038;}i:1;a:1:{s:2:"id";i:125;}i:2;a:1:{s:2:"id";i:1073;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Calculate the an a^n % b where a, b and n are all 32bit integers.</em></strong><br />
[expand title="code"]</p>
<pre>
class Solution {
    /*
     * @param a, b, n: 32bit integers
     * @return: An integer
     */
    public int fastPower(int a, int b, int n) {
        if (n == 1) {
            return a % b;
        } else if (n == 0) {
            return 1 % b;
        } else if (n < 0) {
            return -1;
        }
        //(a * b) % p = (a % p * b % p) % p, 将 a^n % b 分解为 (a^(n/2) * a^(n/2)) % b = ((a^(n/2) % b) * (a^(n/2) % b)) % b, deal with odd n separately.
        long result = fastPower(a, b, n/2);
        //bug1 forget to use long type
        result = result * result % b;
        if (n % 2 == 1) {
            result = result * a % b;
        }
        return (int)result;
        //bug1 forget to cast back to integer
    }
};
</pre>
<p>[/expand]</p>
