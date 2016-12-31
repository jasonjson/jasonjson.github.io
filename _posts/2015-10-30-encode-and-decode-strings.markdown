---
layout: post
title: Encode and Decode Strings
date: 2015-10-30 11:43:26.000000000 -04:00
type: post
published: true
status: publish
categories:
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467813347;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:307;}i:1;a:1:{s:2:"id";i:1510;}i:2;a:1:{s:2:"id";i:1414;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<string> strs) {
        if (strs == null || strs.size() == 0) return "";

        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            sb.append(s.length() + "/" + s);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<string> decode(String s) {
        List<string> result = new ArrayList<>();
        if (s == null || s.length() == 0) return result;
        
        for (int i = 0; i < s.length();) {
            int slash = s.indexOf("/", i);
            int len = Integer.parseInt(s.substring(i, slash));
            result.add(s.substring(slash + 1, slash + len + 1));
            i = slash + len + 1;
        }
        return result;
    }
}
</string></string></string></pre>
<p>[/expand]</p>
