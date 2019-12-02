---
layout: post
title: 139 - Word Break
date: 2015-10-21 12:34:38.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Given a string s and a dictionary of words dict, determine if s can be break into a space-separated sequence of one or more dictionary words.**


``` java
public class Solution {
    public boolean wordBreak(String s, Set<String> wordDict) {
        if (wordDict == null || wordDict.size() == 0) return false;

        int maxLen = 0;
        for (String word : wordDict) {
            maxLen = Math.max(maxLen, word.length());
        }
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (int j = i - 1; i - j <= maxLen && j >= 0; j--) {
            //the length of substring must be smaller than the length of longest word
                if (dp[j] && wordDict.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }
}
```

``` python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False

        max_len = max(map(len, wordDict))
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in reversed(range(i)):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
                    break
                if i - j > max_len:
                    break
        return dp[-1]
```
