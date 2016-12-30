---
layout: post
title: Word Break
date: 2015-10-21 12:34:38.000000000 -04:00
type: post
published: true
status: publish
categories:
- DFS Backtracking
- Dynamic Programming
tags: []
meta:
  _spost_short_title: ''
  _edit_last: '1'
  _wpas_done_all: '1'
  _wpcom_is_markdown: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1457079520;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1414;}i:1;a:1:{s:2:"id";i:93;}i:2;a:1:{s:2:"id";i:1050;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a string s and a dictionary of words dict, determine if s can be break into a space-separated sequence of one or more dictionary words.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</string></pre>
<p>[/expand]</p>
<p>[expand title = "code2"]</p>
<pre>
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
</string></string></pre>
<p>[/expand]</p>
