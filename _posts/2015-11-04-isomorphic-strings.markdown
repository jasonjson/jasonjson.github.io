---
layout: post
title: Isomorphic Strings
date: 2015-11-04 14:33:12.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.**


``` java
public class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s == null || t == null || s.length() != t.length()) return false;

        HashMap<Character, Integer> map1 = new HashMap<Character, Integer>();
        HashMap<Character, Integer> map2 = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            char c1 = s.charAt(i), c2 = t.charAt(i);
            if (!map1.containsKey(c1)) {
                map1.put(c1, i);
            }
            if (!map2.containsKey(c2)) {
                map2.put(c2, i);
            }
            if (map1.size() != map2.size()) {
                return false;
            } else if (map1.get(c1) != map2.get(c2)) {
                return false;
            }
        }
        return true;
    }
}
```

``` python
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        map1, map2 = {}, {}
        for c1, c2 in zip(s, t):
            if map1.get(c1, c2) != c2 or map2.get(c2, c1) != c1:
                return False
            map1[c1], map2[c2] = c2, c1
        return True
```
