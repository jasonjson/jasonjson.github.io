---
layout: post
title: Group Shifted Strings
date: 2015-11-02 09:26:18.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
<p><strong><em>Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:</p>

"abc" -> "bcd" -> ... -> "xyz"</p>
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.</em></strong></p>
``` java
public class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        List<List<String>> result = new ArrayList<List<String>>();
        if (strings == null || strings.length == 0) return result;
        
        HashMap<String, List<String>> map = new HashMap<String, List<String>>();
        Arrays.sort(strings);
        for (String s : strings) {
            String key = ""; //the distance between nearby chars should be the same
            for (int i = 1; i < s.length(); i++) {
                key += (s.charAt(i) - s.charAt(i-1) + 26) % 26;//deal with z -> a
            }
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<String>());
            }
            map.get(key).add(s);
        }
        for (List<String> list : map.values()) {
            result.add(list);
        }
        return result;
    }
}
```
