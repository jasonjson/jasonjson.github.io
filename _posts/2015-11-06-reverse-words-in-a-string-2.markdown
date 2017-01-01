---
layout: post
title: Reverse Words in a String
date: 2015-11-06 11:37:05.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464657127;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:89;}i:1;a:1:{s:2:"id";i:577;}i:2;a:1:{s:2:"id";i:87;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an input string, reverse the string word by word.<br />
For example,<br />
Given s = "the sky is blue",<br />
return "blue is sky the".</em></strong></p>
<p>[expand title="code1"]</p>
<pre>
public class Solution {
    public String reverseWords(String s) {
        if (s == null || s.length() == 0) return "";
        s = s.replaceAll("\s+", " ");//replace multiple white spaces with one whitespace
        char[] chars = s.trim().toCharArray();
        int start = 0;
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == ' ') {
                if (i > 0 && chars[i-1] == ' ') {
                    continue;
                } else {
                    reverse(chars, start, i - 1);
                    start = i + 1;
                }
            }
        }
        reverse(chars, start, chars.length - 1);
        reverse(chars, 0, chars.length - 1);
        return String.valueOf(chars);
    }

    public void reverse(char[] chars, int lo, int hi) {
        while (lo <= hi) {
            char temp = chars[lo];
            chars[lo] = chars[hi];
            chars[hi] = temp;
            lo ++;
            hi --;
        }
    }
}
</pre>
<p>[/expand]<br />
[expand title="code2"]</p>
<pre>
public class Solution {
    /**
     * @param s : A string
     * @return : A string
     */
    public String reverseWords(String s) {
        // write your code
        if (s == null || s.length() == 0) return "";
        
        String[] strs = s.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = strs.length - 1; i >= 0; i--) {
            if (strs[i].length() == 0) continue;
            sb.append(strs[i]);
            if (i != 0) sb.append(" ");
        } 
        return sb.toString();
    }
}
</pre>
<p>[/expand]</p>
