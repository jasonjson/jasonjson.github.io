---
layout: post
title: 290 - Word Pattern
date: 2015-11-27 16:47:45.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a pattern and a string str, find if str follows the same pattern.**


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

``` python
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern or not str:
            return False

        p_map, s_map = {}, {}
        str_list = str.split(" ")
        if len(pattern) != len(str_list):
            return False
        for p, s in zip(pattern, str_list):
            if p_map.get(p, s) != s or s_map.get(s, p) != p:
                return False
            p_map[p], s_map[s] = s, p
        return True
```
