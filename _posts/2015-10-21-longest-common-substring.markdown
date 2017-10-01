---
layout: post
title: Longest Common Substring
date: 2015-10-21 02:12:17.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
- String
author: Jason
---
<p><strong><em>Given two strings, find the longest common substring. Return the length of it.</em></strong></p>


``` java
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
```

``` java
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
```
