---
layout: post
title: Add Digits
date: 2015-10-31 10:40:28.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463180561;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:127;}i:1;a:1:{s:2:"id";i:559;}i:2;a:1:{s:2:"id";i:125;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.<br />
For example:<br />
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.<br />
Follow up:<br />
Could you do it without any loop/recursion in O(1) runtime?</em></strong><br />
[expand title="Best"]</p>
<pre>
public class Solution {
    public int addDigits(int num) {
        if (num == 0) return 0;
        return num % 9 == 0 ? 9 : num % 9;//观察结果 与9相关
    }
}
</pre>
<p>[/expand]<br />
[expand title="String"]</p>
<pre>
public class Solution {
    public int addDigits(int num) {
        String s = String.valueOf(num);
        while (s.length() > 1) {
            int sum = 0;
            for (char c : s.toCharArray()) {
                sum += Character.getNumericValue(c);
            }
            s = String.valueOf(sum);
        }
        return Integer.parseInt(s);
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title="Integer"]</p>
<pre>
public class Solution {
    public int addDigits(int num) {
        int temp = 0;
        while (num > 0) {
            temp += num % 10;
            if (temp >= 10) {
                temp = temp % 10 + temp / 10;
            } 
            num /= 10;
        }
        return temp;
    }
}
</pre>
<p>[/expand]</p>
