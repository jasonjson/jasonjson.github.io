---
layout: post
title: Swap two digits in a integer
date: 2015-11-14 15:08:06.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465389981;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:200;}i:1;a:1:{s:2:"id";i:559;}i:2;a:1:{s:2:"id";i:505;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Swap two digits within a integer. For instance, 123456, swap 2nd and 4th digit, output 125436</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public static void main(String[] args) {
        int n = 123456;
        System.out.println(swap(n, 2, 4));
    }
    public static int swap(int n, int i, int j) {
        int len = 0, temp = n;
        while (temp > 0) {
            len ++;
            temp /= 10;
        }
        int digit1 = getDigit(n, i, len);
        int digit2 = getDigit(n, j, len);
        int base1 = 1, base2 = 1;
        for (int k = i; k < len - 1; k++) {
            base1 *= 10;
        }
        for (int k = j; k < len - 1; k++) {
            base2 *= 10;
        }
        return n - digit1 * base1 - digit2 * base2 + digit2 * base1 + digit1 * base2;
    }

    public static int getDigit(int n, int i, int len) {
        int base = 1;
        for (int k = i; k < len - 1; k++) {
            base *= 10;
        }
        return (n / base) % 10;
    }
}
</pre>
<p>[/expand]</p>
