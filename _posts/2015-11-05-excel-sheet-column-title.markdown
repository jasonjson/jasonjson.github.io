---
layout: post
title: Excel Sheet Column Title
date: 2015-11-05 11:43:27.000000000 -05:00
tags:
- Algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given a positive integer, return its corresponding column title as appear in an Excel sheet.</em></strong></p>


``` java
public class Solution {
    public String convertToTitle(int n) {
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            int digit = n % 26;
            n /= 26;
            if (digit == 0) {//deal with 26 separately
                sb.append("Z");
                n --;
            } else {
                sb.append((char)(digit - 1 + 'A'));
            }
        }
        return sb.reverse().toString();
    }
}
```
