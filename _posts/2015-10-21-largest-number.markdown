---
layout: post
title: Largest Number
date: 2015-10-21 14:24:22.000000000 -04:00
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
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1456859989;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1187;}i:1;a:1:{s:2:"id";i:421;}i:2;a:1:{s:2:"id";i:416;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a list of non negative integers, arrange them such that they form the largest number.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     *@param num: A list of non negative integers
     *@return: A string
     */
    public String largestNumber(int[] num) {
        // write your code here
        if (num == null || num.length == 0) return "";
        
        List<string> list = new ArrayList<string>();
        for (int n : num) {
            list.add(String.valueOf(n));
        }        
        Collections.sort(list, new Comparator<string>() {
            public int compare (String a, String b) {
                return (b + a).compareTo(a + b);
            }
        });
        StringBuilder sb = new StringBuilder();
        for (String s : list) {
            sb.append(s);
        }
        if (sb.charAt(0) == '0') {
            return "0";
        } else {
            return sb.toString();
        }
    }
}
</string></string></string></pre>
<p>[/expand]</p>
