---
layout: post
title: 44 - Wildcard Matching
date: 2015-10-21 02:15:18.000000000 -04:00
tags:
- Leetcode
categories:
- String
author: Jason
---
**Implement wildcard pattern matching with support for '?' and '*'.**


``` java
public class Solution {
    public static boolean isMatch(String s, String p) {
        int lenS = s.length(), lenP = p.length();
        boolean[][] d = new boolean[lenS + 1][lenP + 1];
        d[0][0] = true;
        for(int i = 1; i <= lenP; i++){
            if(p.charAt(i - 1) == '*') d[0][i] = d[0][i - 1];
        }

        for(int i = 1; i <= lenS; i++){
            for(int j = 1; j <= lenP; j++){
                if(s.charAt(i - 1) == p.charAt(j - 1) || p.charAt(j - 1) == '?'){
                    d[i][j] = d[i - 1][j - 1];
                } else if(p.charAt(j - 1) == '*'){
                //find if there is a s[0, k - 1] that
                //matches p[0, j - 1] for (k : 0 to i)
                    for(int k = 0; k <= i; k++){
                        if(d[k][j - 1]) {
                            d[i][j] = true;
                            break;
                        }
                    }
                }
            }
        }
        return d[lenS][lenP];
    }
}
```

``` python
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """


        is_match = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        is_match[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == "*":
                is_match[0][j] = is_match[0][j - 1]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    is_match[i][j] = is_match[i - 1][j - 1]
                elif p[j - 1] == "*":
                    for k in range(i + 1):
                        if is_match[k][j - 1]:
                            is_match[i][j] = True
                            break

        return is_match[-1][-1]
```
