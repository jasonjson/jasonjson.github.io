---
layout: post
title: Implement strStr()
date: 2015-10-21 02:10:21.000000000 -04:00
type: post
published: true
status: publish
categories:
- String
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465710670;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1501;}i:1;a:1:{s:2:"id";i:410;}i:2;a:1:{s:2:"id";i:398;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Implement strStr().Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.</em></strong></p>
<p><a href="https://www.youtube.com/watch?v=GTJr8OvyEVQ">read more</a><br />
[expand title = "KMP"]</p>
<pre>
public class Solution {
    public int strStr(String haystack, String needle) {
        int len1 = haystack.length(), len2 = needle.length();
        int[] key = new int[len2];
        for (int i = 1; i < len2; i++) {
            int j = key[i - 1];
            while (j != 0 && needle.charAt(i) != needle.charAt(j)) {
                j = key[j - 1];
            }
            key[i] = j + (needle.charAt(i) == needle.charAt(j) ? 1 : 0);//一定要括号起来！不然报错
        }
        int i = 0, j = 0;
        while (i < len2 && j < len1) {//i points to index in needle, j points to index at haystack
            if (i > 0 && needle.charAt(i) != haystack.charAt(j)) {
                i = key[i - 1];
            } else {
                i += (needle.charAt(i) == haystack.charAt(j) ? 1 : 0);
                j ++;
            }
        }
        return i == len2 ? j - len2 : -1;
    }
}
</pre>
<p>[/expand]<br />
[expand title="code"]</p>
<pre>
public class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0) return 0;

        int len1 = haystack.length(), len2 = needle.length();
        for (int i = 0; i + len2 - 1 < len1; i++) {
            for (int j = 0; j < len2; j++) {
                if (needle.charAt(j) != haystack.charAt(i + j)) {
                    break;
                }
                if (j == len2 - 1) {
                    return i;
                }
            }
        }
        return -1;
    }
}
</pre>
<p>[/expand]</p>
