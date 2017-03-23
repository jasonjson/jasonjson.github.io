---
layout: post
title: Valid Number
date: 2015-10-26 17:19:21.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
- Integer
author: Jason
---
<p><strong><em>Validate if a given string is numeric.</em></strong></p>


``` java
public class Solution {
    /**
     * @param s the string that represents a number
     * @return whether the string is a valid number
     */
    public boolean isNumber(String s) {
        // Write your code here
        if (s == null || s.length() == 0) return false;
        
        boolean dot = false, exp = false, num = false;        
        s = s.trim();
        int i = 0;
        if (i < s.length() && (s.charAt(i) == '+' || s.charAt(i) == '-')) {
            i ++;
        }
        for (; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                num = true;
            } else if (c == '.') {
                if (dot || exp) {
                    return false;
                } else {
                    dot = true;
                }
            } else if (c == 'e') {
                if (exp || !num) {
                    return false;
                } else {
                    exp = true;
                    num = false;
                }
            } else if (c == '+' || c == '-') {
                if (s.charAt(i-1) != 'e') {
                    return false;
                }
            } else {
                return false;
            }
        }
        return num;
    }
}
```
