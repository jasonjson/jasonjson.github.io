---
layout: post
title: Largest sibling
date: 2015-10-25 20:08:38.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
tags:
- Cloudera OA
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468494719;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:557;}i:1;a:1:{s:2:"id";i:1386;}i:2;a:1:{s:2:"id";i:433;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a number, find the largest sibling</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class solution {
    public int largestSibling(int num) {
        char[] chars = String.valueOf(num).toCharArray();
        Arrays.sort(chars);
        long result = 0;
        for (int i = chars.length - 1; i >= 0; i --) {
            result = result * 10 + Character.getNumericValue(chars[i]);
        }
        if (result > Integer.MAX_VALUE) {
            return Integer.MAX_VALUE;
        } else {
            return (int)result;//cast long back to int!!!
        }
    }
}
</pre>
<p>[/expand]</p>
