---
layout: post
title: Group Shifted Strings
date: 2015-11-02 09:26:18.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466714607;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:433;}i:1;a:1:{s:2:"id";i:438;}i:2;a:1:{s:2:"id";i:1208;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:<br />
"abc" -> "bcd" -> ... -> "xyz"<br />
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public List<List<string>> groupStrings(String[] strings) {
        List<List<string>> result = new ArrayList<List<string>>();
        if (strings == null || strings.length == 0) return result;
        
        HashMap<String, List<string>> map = new HashMap<String, List<string>>();
        Arrays.sort(strings);
        for (String s : strings) {
            String key = ""; //the distance between nearby chars should be the same
            for (int i = 1; i < s.length(); i++) {
                key += (s.charAt(i) - s.charAt(i-1) + 26) % 26;//deal with z -> a
            }
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<string>());
            }
            map.get(key).add(s);
        }
        for (List<string> list : map.values()) {
            result.add(list);
        }
        return result;
    }
}
</string></string></string></string></string></string></string></pre>
<p>[/expand]</p>
