---
layout: post
title: Additive Number
date: 2015-11-18 09:31:17.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469168956;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:472;}i:1;a:1:{s:2:"id";i:390;}i:2;a:1:{s:2:"id";i:1357;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Additive number is a positive integer whose digits can form additive sequence.<br />
A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
import java.math.BigInteger;
public class Solution {
    public boolean isAdditiveNumber(String num) {
        if (num == null || num.length() < 3) return false;
        
        for (int i = 1; i <= num.length() / 2; i++) {
            if (num.charAt(0) == '0' && i > 1) break;//0 is the starting point of the first number
            BigInteger a = new BigInteger(num.substring(0, i));
            for (int j = 1; Math.max(i, j) <= num.length() - i - j; j++) {
                if (num.charAt(i) == '0' && j > 1) break;//i is the starting point of the second number
                BigInteger b = new BigInteger(num.substring(i, i + j));
                if (isValid(num.substring(i + j), a, b)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    public boolean isValid(String num, BigInteger a, BigInteger b) {
        if (num.length() == 0) return true;
        
        b = a.add(b);
        a = b.subtract(a);
        String c = String.valueOf(b);
        return num.startsWith(c) && isValid(num.substring(c.length()), a, b);
    }
}
</pre>
<p>[/expand]</p>
