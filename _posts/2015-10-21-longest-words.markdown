---
layout: post
title: Longest Words
date: 2015-10-21 12:59:11.000000000 -04:00
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
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1462287715;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:595;}i:1;a:1:{s:2:"id";i:307;}i:2;a:1:{s:2:"id";i:390;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a dictionary, find all of the longest words in the dictionary.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
class Solution {
    public ArrayList<string> longestWords(String[] dictionary) {
        ArrayList<string> result = new ArrayList<string>();
        if (dictionary == null) return result;
        
        int maxLen = 0;
        for (String str : dictionary) {
            if (str.length() > maxLen) {
                result.clear();
                result.add(str);
                maxLen = str.length();
            } else if (str.length() == maxLen) {
                result.add(str);
            }
        }
        return result;
    }
};
</string></string></string></pre>
<p>[/expand]</p>
