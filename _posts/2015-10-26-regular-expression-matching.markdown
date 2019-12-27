---
layout: post
title: 10 - Regular Expression Matching
date: 2015-10-26 20:27:13.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Implement regular expression matching.**
[reference](http://bangbingsyb.blogspot.com/2014/11/leetcode-regular-expression-matching.html")


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

``` python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1, l2 = len(s), len(p)
        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
        dp[0][0] = True
        for j in range(1, l2 + 1):
            if j > 1 and p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                        dp[i][j] |= dp[i - 1][j]
        return dp[-1][-1]
```
