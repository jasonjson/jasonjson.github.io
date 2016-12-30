---
layout: post
title: Word Pattern II
date: 2015-10-21 14:48:16.000000000 -04:00
type: post
published: true
status: publish
categories:
- DFS Backtracking
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468750090;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1668;}i:1;a:1:{s:2:"id";i:1208;}i:2;a:1:{s:2:"id";i:2073;}}}}
  _inbound_impressions_count: '0'
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a pattern and a string str, find if str follows the same pattern.You are given a pattern, such as [a b a b]. You are also given a string, example "redblueredblue".</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public boolean wordPatternMatch(String pattern, String str) {
        HashMap<Character, String> map = new HashMap<Character, String>();
        return helper(pattern, str, map);
    }
    
    public boolean helper(String pattern, String str, HashMap<Character, String> map) {
        if (pattern.length() == 0) {
            return str.length() == 0;
        }
        char pch = pattern.charAt(0);
        if (!map.containsKey(pch)) {
            for (int i = 1; i <= str.length(); i++) {
                String s = str.substring(0, i);
                if (!map.containsValue(s)) {//string不能已经出现在map中
                //for test case ("aa", "ab") two pairs in map a - b, a - b, which is wrong, we need to check if the map has the value already
                    map.put(pch, s);
                    if (helper(pattern.substring(1), str.substring(s.length()), map)) {
                        return true;
                    } else {
                        map.remove(pch);
                    }
                }
            }
        } else {
            String s = map.get(pch);
            if (!str.startsWith(s)) {
                return false;
            } else {
                return helper(pattern.substring(1), str.substring(s.length()), map);
            }
        }
        return false;
    }
}
</pre>
<p>[/expand]</p>
