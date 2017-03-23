---
layout: post
title: One Edit Distance
date: 2015-11-05 15:30:45.000000000 -05:00
tags:
- Algorithm
categories:
- Brain teaser
- String
author: Jason
---
<p><strong><em>Given two strings S and T, determine if they are both one edit distance apart.</em></strong></p>


``` java
//The basic idea is we keep comparing s and t from the beginning, once there's a difference, we try to replace s(i) with t(j) or insert t(j) to s(i) and see if the rest are the same.
public class Solution {
    public boolean isOneEditDistance(String s, String t) {
        int len1 = s.length(), len2 = t.length();
        if (len1 > len2) {
            return isOneEditDistance(t, s);
        }
        if (len1 + 1 < len2) {
            return false;
        }
        for (int i = 0; i < len1; i++) {
            if (s.charAt(i) != t.charAt(i)) {
                return s.substring(i + 1).equals(t.substring(i + 1)) || s.substring(i).equals(t.substring(i + 1));
            }
        }
        return len1 + 1 == len2;//走到这一步的唯一可能就是前面len-1个字符都完全一样,为了保证有一个distance,t必须比s多一个字符
    }
}
```
