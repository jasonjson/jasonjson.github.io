---
layout: post
title: Word Pattern II
date: 2015-10-21 14:48:16.000000000 -04:00
tags: algorithm
categories:
- DFS Backtracking
author: Jason
---
<p><strong><em>Given a pattern and a string str, find if str follows the same pattern.You are given a pattern, such as [a b a b]. You are also given a string, example "redblueredblue".</em></strong></p>


``` java
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
```
