---
layout: post
title: Longest Common Prefix
date: 2015-11-15 12:24:19.000000000 -05:00
tags:
- Algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Write a function to find the longest common prefix string amongst an array of strings.</em></strong></p>


``` java
public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        String s = strs[0];
        for (int i = 1; i < strs.length; i++) {
            int j = 0;
            while (j < s.length() && j < strs[i].length() && s.charAt(j) == strs[i].charAt(j)) {
                j ++;
            }
            s = s.substring(0, j);
        }
        return s;
    }
}
```
``` java
public class Solution {
    /**
     * @param strs: A list of strings
     * @return: The longest common prefix
     */
    public String longestCommonPrefix(String[] strs) {
        // write your code here
        if (strs == null || strs.length == 0) return "";
        
        Arrays.sort(strs);
        String head = strs[0], tail = strs[strs.length - 1];
        int i = 0;
        for (; i < head.length(); i++) {
            if (head.charAt(i) != tail.charAt(i)) {
                break;
            }
        }
        return head.substring(0, i);
    }
}
```
