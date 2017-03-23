---
layout: post
title: Repeated DNA Sequences
date: 2015-11-04 17:31:35.000000000 -05:00
tags:
- Algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.</p>

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.</em></strong></p>
``` java
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
```
