---
layout: post
title: Longest Common Substring
date: 2015-10-21 02:12:17.000000000 -04:00
type: post
published: true
status: publish
categories:
- Dynamic Programming
- String
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465857570;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:396;}i:1;a:1:{s:2:"id";i:1587;}i:2;a:1:{s:2:"id";i:545;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given two strings, find the longest common substring. Return the length of it.</em></strong></p>
<p>[expand title = "dp"]</p>
<pre>
public class Solution {
    /**
     * @param A, B: Two string.
     * @return: the length of the longest common substring.
     */
    public int longestCommonSubstring(String A, String B) {
        if (A == null || B == null) return -1;
        if (A.length() == 0 || B.length() == 0 ) return 0;
        
        int maxLen = 0;
        int[][] lcs = new int[A.length() + 1][B.length() + 1];
        //the length of longest common substring ending with A.charAt(i) and B.charAt(j)
        for (int i = 1; i <= A.length(); i++) {
            for (int j = 1; j <= B.length(); j++) {
                if (A.charAt(i-1) == B.charAt(j-1)) {
                    lcs[i][j] = lcs[i-1][j-1] + 1;
                }
                maxLen = Math.max(maxLen, lcs[i][j]);
            }
        }
        return maxLen;
    }
}
</pre>
<p>[/expand]<br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param A, B: Two string.
     * @return: the length of the longest common substring.
     */
    public int longestCommonSubstring(String A, String B) {
        // write your code here
        if(A == "" || B == "") return 0;
        int maxLen = 0;
        for(int i = 0; i < A.length(); i++){
            for(int j = 0; j < B.length(); j++){
                int len = 0;
                //use len to control the position in String B
                while(i + len < A.length() && j + len < B.length() && A.charAt(i+len) == B.charAt(j+len)){
                    len++;
                }
                maxLen = Math.max(maxLen, len);
            }
        }
        return maxLen;
    }
}
</pre>
<p>[/expand]</p>
