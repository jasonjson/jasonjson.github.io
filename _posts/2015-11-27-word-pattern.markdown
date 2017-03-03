---
layout: post
title: Word Pattern
date: 2015-11-27 16:47:45.000000000 -05:00
tags: algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given a pattern and a string str, find if str follows the same pattern.</em></strong></p>


``` java
public class Solution {
    public boolean wordPattern(String pattern, String str) {
        if (pattern.length() == 0 || str.length() == 0) return false;
        
        String[] words = str.split(" ");//split empty spaces, not ""
        if (pattern.length() != words.length) { 
            return false;
        }
        Map<Character, String> map = new HashMap<Character, String>();
        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern.charAt(i);
            if (!map.containsKey(c) && map.containsValue(words[i])) {
                return false;
            } else if (map.containsKey(c) && !map.get(c).equals(words[i])) {
                return false;
            } else {
                map.put(c, words[i]);
            }
        }
        return true;
    }
}
```
