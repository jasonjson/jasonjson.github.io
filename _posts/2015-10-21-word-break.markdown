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
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if not wordDict:
            return False
        max_len = max([len(word) for word in wordDict])
        dp = [False] * (len(s) + 1)
        dp[0] = True #empty string is always true
        for i in xrange(1, len(s) + 1):
            j = i - 1
            while j >= 0 and i - j <= max_len:
                if dp[j] and s[j : i] in wordDict:
                    dp[i] = True
                    break
                j -= 1
        return dp[-1]
```

