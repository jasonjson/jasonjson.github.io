---
layout: post
title: Longest Palindromic Substring
date: 2015-10-21 02:14:16.000000000 -04:00
tags:
- Algorithm
categories:
- Palindrome
- String
author: Jason
---
**Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.**


``` java
public class Solution {
    public String longestPalindrome(String s) {
        if(s == null || s.length() == 0) return "";
        int start = 0, maxLen = 0;
        boolean[][] isPalin = new boolean[s.length()][s.length()];
        for (int i = s.length() - 1; i >= 0; i--) {
            for (int j = i; j < s.length(); j++) {
                if (s.charAt(i) == s.charAt(j) && (j - i <= 2 || isPalin[i+1][j-1])) {
                    isPalin[i][j] = true;//only update maxLen when isPalin[i][j] is true
                    if (maxLen < j - i + 1) {
                        maxLen = j - i + 1;
                        start = i;
                    }
                }
            }
        }
        return s.substring(start, start + maxLen);
    }
}
```

``` java
public class Solution {
    public String longestPalindrome(String s) {
        if(s == null || s.length() == 0) return s;
        int maxLen = 1, start = 0;
        for(int i = 0; i < s.length(); i++){
            int lo = i, hi = i + 1;
            //even case
            while(lo >=0 && hi < s.length() && s.charAt(lo) == s.charAt(hi)){
                if(hi - lo + 1 > maxLen){
                    maxLen = hi - lo + 1;
                    start = lo;
                }
                lo--; //!lo -- not lo ++
                hi++;
            }   
            //odd case, i is the mid position    
            lo = i - 1; hi = i + 1;
            while(lo >=0 && hi < s.length() && s.charAt(lo) == s.charAt(hi)){
                if(hi - lo + 1 > maxLen){
                    maxLen = hi - lo + 1;
                    start = lo;
                }
                lo--;
                hi++;
            }
        }
        return s.substring(start, start + maxLen);
    }
```

``` python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        max_len, start = 1, 0 #max_len default to 1
        for i, char in enumerate(s):
            lo, hi = i, i + 1
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                if hi - lo + 1 > max_len:
                    max_len = hi - lo + 1
                    start = lo
                lo -= 1
                hi += 1

            lo, hi = i - 1, i + 1
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                if hi - lo + 1 > max_len:
                    max_len = hi - lo + 1
                    start = lo
                lo -= 1
                hi += 1

        return s[start:start + max_len]
```
