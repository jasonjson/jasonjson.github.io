---
layout: post
title: Encode and Decode Strings
date: 2015-10-30 11:43:26.000000000 -04:00
tags:
- Algorithm
categories:
- Data Structure
author: Jason
---
<p><strong><em>Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.</em></strong></p>


``` java
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
```
