---
layout: post
title: Interleaving String
date: 2015-10-21 12:49:37.000000000 -04:00
type: post
published: true
status: publish
categories:
- Dynamic Programming
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466367939;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1050;}i:1;a:1:{s:2:"id";i:79;}i:2;a:1:{s:2:"id";i:450;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * Determine whether s3 is formed by interleaving of s1 and s2.
     * @param s1, s2, s3: As description.
     * @return: true or false.
     */
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1 == null && s2 == null && s3 == null) return true;
        int l1 = s1.length(), l2 = s2.length(), l3 = s3.length();
        if (l1 == 0 && l2 == 0 && l3 == 0) return true;
        if (l1 + l2 != l3) return false;
        
        boolean[][] dp = new boolean[l1+1][l2+1];
        //dp[i][j] : s1.substring(0, i) and s2.substring(0, j) matches 
        //s3.substring(0, i+j-1)
        dp[0][0] = true;//base case !!
        for (int i = 1; i <= l1; i++) {
            dp[i][0] = s1.charAt(i-1) == s3.charAt(i-1) && dp[i-1][0];
        }
        
        for (int j = 1; j <= l2; j++) {
            dp[0][j] = s2.charAt(j-1) == s3.charAt(j-1) && dp[0][j-1];
        }
        
        for (int i = 1; i <= l1; i++) {
            for (int j = 1; j <= l2; j++) {
                boolean case1 = s1.charAt(i-1) == s3.charAt(i + j - 1) && dp[i-1][j];
                boolean case2 = s2.charAt(j-1) == s3.charAt(i + j - 1) && dp[i][j-1];
                dp[i][j] = case1 || case2;
            }
        }
        return dp[l1][l2];
    }
}
</pre>
<p>[/expand]</p>
