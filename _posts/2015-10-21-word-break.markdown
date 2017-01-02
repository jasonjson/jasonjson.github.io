---
layout: post
title: Word Break
date: 2015-10-21 12:34:38.000000000 -04:00
categories:
- DFS Backtracking
- Dynamic Programming
author: Jason
---
<p><strong><em>Given a string s and a dictionary of words dict, determine if s can be break into a space-separated sequence of one or more dictionary words.</em></strong></p>


``` java
public class Solution {
    public boolean wordBreak(String s, Set<string> wordDict) {
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
``` java
public class Solution {
    /**
     * @param s: A string s
     * @param dict: A dictionary of words dict
     */
    public boolean wordBreak(String s, Set<string> dict) {
        if (s == null || s.length() == 0) return true;
        
        return helper(s, dict);
    }
    
    public boolean helper(String s, Set<string> dict) {
        if (dict.contains(s)) {
            return true;
        }
        for (int i = 1; i <= s.length(); i++) {
            String sub = s.substring(0, i);
            if (dict.contains(sub) && helper(s.substring(i), dict)) {
                return true;
            }
        }
        return false;
    }
}//Memory Limit Exceed, use dp instead
```
