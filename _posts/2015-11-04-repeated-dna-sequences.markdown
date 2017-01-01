---
layout: post
title: Repeated DNA Sequences
date: 2015-11-04 17:31:35.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464670644;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1510;}i:1;a:1:{s:2:"id";i:438;}i:2;a:1:{s:2:"id";i:1208;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.<br />
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public List<string> findRepeatedDnaSequences(String s) {
        List<string> result = new ArrayList<>();
        if (s == null || s.length() == 0) return result;
        
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i + 9 < s.length(); i++) {
            String newS = s.substring(i, i + 10);
            if (map.containsKey(newS) && map.get(newS) <= 1) {
                result.add(newS);
            }
            map.put(newS, map.getOrDefault(newS, 0) + 1);
        }
        return result;
    }
}
</string></string></pre>
<p>[/expand]</p>
