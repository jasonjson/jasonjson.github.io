---
layout: post
title: Regular Expression Matching
date: 2015-10-26 20:27:13.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
- Dynamic Programming
author: Jason
---
<p><strong><em>Implement regular expression matching.</em></strong></p>


<p><a href="http://bangbingsyb.blogspot.com/2014/11/leetcode-regular-expression-matching.html">See detailed explanation</a></p>

``` java
public class Solution {
    /**
     * @param s: A string 
     * @param p: A string includes "." and "*"
     * @return: A boolean
     */
    public boolean isMatch(String s, String p) {
        if (s.length() == 0) return p.length() == 0;
        
        int lens = s.length(), lenp = p.length();
        
        boolean[][] match = new boolean[lens + 1][lenp + 1];
        match[0][0] = true;
        for (int j = 1; j <= lenp; j++) {
            if (j > 1 && p.charAt(j-1) == '*') {
                match[0][j] = match[0][j-2];
            }
        }
        for (int i = 1; i <= lens; i++) {
            for (int j = 1; j <= lenp; j++) {
                if (p.charAt(j-1) == '.' || p.charAt(j-1) == s.charAt(i-1)) {
                    match[i][j] = match[i-1][j-1];
                } else if (j > 1 && p.charAt(j-1) == '*') {
                    if (s.charAt(i-1) == p.charAt(j-2) || p.charAt(j-2) == '.') {
                        match[i][j] = match[i][j-2] || match[i-1][j];
                    } else {
                        match[i][j] = match[i][j-2];
                    }
                }
            }
        }
        return match[lens][lenp];
    }
}
```
