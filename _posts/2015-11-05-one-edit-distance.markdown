---
layout: post
title: One Edit Distance
date: 2015-11-05 15:30:45.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
- String
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469240220;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:410;}i:1;a:1:{s:2:"id";i:398;}i:2;a:1:{s:2:"id";i:1501;}}}}
  _wpas_done_all: '1'
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given two strings S and T, determine if they are both one edit distance apart.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
//The basic idea is we keep comparing s and t from the beginning, once there's a difference, we try to replace s(i) with t(j) or insert t(j) to s(i) and see if the rest are the same.
public class Solution {
    public boolean isOneEditDistance(String s, String t) {
        int len1 = s.length(), len2 = t.length();
        if (len1 > len2) {
            return isOneEditDistance(t, s);
        }
        if (len1 + 1 < len2) {
            return false;
        }
        for (int i = 0; i < len1; i++) {
            if (s.charAt(i) != t.charAt(i)) {
                return s.substring(i + 1).equals(t.substring(i + 1)) || s.substring(i).equals(t.substring(i + 1));
            }
        }
        return len1 + 1 == len2;//走到这一步的唯一可能就是前面len-1个字符都完全一样,为了保证有一个distance,t必须比s多一个字符
    }
}
</pre>
<p>[/expand]</p>
