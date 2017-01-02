---
layout: post
title: Word Break II
date: 2015-11-06 14:27:27.000000000 -05:00
categories:
- DFS Backtracking
author: Jason
---
<p><strong><em>Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.</p>

Return all such possible sentences.</em></strong></p>
``` java
public class Solution {
    public List<string> wordBreak(String s, Set<string> wordDict) {
        List<string> result = new ArrayList<string>();
        if (wordDict == null || wordDict.size() == 0) return result;
        
        boolean[] dp = getWord(s, wordDict);
        if (!dp[s.length()]) {
            return result;
        } else {
            helper(s, wordDict, "", result);
            return result;
        }
    }
    
    public boolean[] getWord(String s, Set<string> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (int j = i; j >= 0; j --) {
                if (dp[j] && wordDict.contains(s.substring(j,i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp;
    }
    
    public void helper(String s, Set<string> wordDict, String path, List<string> result) {
        if (s.length() == 0) {
            result.add(new String(path.substring(1)));
            return;
        }
        for (int i = 1; i <= s.length(); i++) {
            String newS = s.substring(0, i);
            if (wordDict.contains(newS)) {
                helper(s.substring(i), wordDict, path + " " + newS, result);
            }
        }
    }
}
```
