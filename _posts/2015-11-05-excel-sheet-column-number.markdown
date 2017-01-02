---
layout: post
title: Excel Sheet Column Number
date: 2015-11-05 11:50:50.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given a column title as appear in an Excel sheet, return its corresponding column number.</em></strong></p>


``` java
public class Solution {
    public int titleToNumber(String s) {
        if (s == null || s.length() == 0) return 0;
        int result = 0;
        for (char c : s.toCharArray()) {
            result = result * 26 + (int)(c - 'A' + 1); 
        }
        return result;
    }
}
```
