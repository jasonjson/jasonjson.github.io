---
layout: post
title: Reverse Words in a String
date: 2015-11-06 11:37:05.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given an input string, reverse the string word by word.<br />

For example,<br />
Given s = "the sky is blue",<br />
return "blue is sky the".</em></strong></p>
``` java
public class Solution {
    public String reverseWords(String s) {
        if (s == null || s.length() == 0) return "";
        s = s.replaceAll("\s+", " ");//replace multiple white spaces with one whitespace
        char[] chars = s.trim().toCharArray();
        int start = 0;
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == ' ') {
                if (i > 0 && chars[i-1] == ' ') {
                    continue;
                } else {
                    reverse(chars, start, i - 1);
                    start = i + 1;
                }
            }
        }
        reverse(chars, start, chars.length - 1);
        reverse(chars, 0, chars.length - 1);
        return String.valueOf(chars);
    }

    public void reverse(char[] chars, int lo, int hi) {
        while (lo <= hi) {
            char temp = chars[lo];
            chars[lo] = chars[hi];
            chars[hi] = temp;
            lo ++;
            hi --;
        }
    }
}
```

``` java
public class Solution {
    /**
     * @param s : A string
     * @return : A string
     */
    public String reverseWords(String s) {
        // write your code
        if (s == null || s.length() == 0) return "";
        
        String[] strs = s.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = strs.length - 1; i >= 0; i--) {
            if (strs[i].length() == 0) continue;
            sb.append(strs[i]);
            if (i != 0) sb.append(" ");
        } 
        return sb.toString();
    }
}
```
