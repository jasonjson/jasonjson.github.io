---
layout: post
title: Roman to Integer
date: 2015-10-21 14:21:28.000000000 -04:00
categories:
- Integer
author: Jason
---
<p><strong><em>Given a roman numeral, convert it to an integer. The answer is guaranteed to be within the range from 1 to 3999.</em></strong></p>


``` java
public class Solution {
    public int romanToInt(String s) {
        if (s == null || s.length() == 0) return 0;
                char[] roman = {'I','V','X','L','C','D','M'};
        int result = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            if (c == 'I') {
                if (i < s.length() - 1 && (s.charAt(i + 1) == 'V' || s.charAt(i + 1) == 'X')) {
                    result -= 1;
                } else {
                    result += 1;     
                }
            } else if (c == 'V') {
                result += 5;
            } else if (c == 'X') {
                if (i < s.length() - 1 && (s.charAt(i + 1) == 'L' || s.charAt(i + 1) == 'C')) { 
                    result -= 10;
                } else {
                    result += 10;
                }
            } else if (c == 'L') {
                result += 50;
            } else if (c == 'C') {
                if (i < s.length() - 1 && (s.charAt(i + 1) == 'D' || s.charAt(i + 1) == 'M')) { 
                    result -= 100;
                } else {
                    result += 100;
                }
            } else if (c == 'D') {
                result += 500;
            } else if (c == 'M') {
                result += 1000;
            }
        }
        return result;
    }
}
```
