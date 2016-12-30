---
layout: post
title: Longest Palindromic Substring
date: 2015-10-21 02:14:16.000000000 -04:00
type: post
published: true
status: publish
categories:
- Palindrome
- String
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464791514;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:393;}i:1;a:1:{s:2:"id";i:1422;}i:2;a:1:{s:2:"id";i:1587;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.</em></strong></p>
<p>[expand title = "dp"]</p>
<pre>
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
</pre>
<p>[/expand]<br />
[expand title="code"]</p>
<pre>
public class Solution {   
    public String longestPalindrome(String s) {
        if(s == null || s.length() <= 1) return s;
        int maxLen = 0, start = 0;
        for(int i = 1; i < s.length(); i++){
            int lo = i - 1, hi = i;
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
</pre>
<p>[/expand]</p>
