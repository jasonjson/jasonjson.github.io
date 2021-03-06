---
layout: post
title: 14 - Longest Common Prefix
date: 2015-11-15 12:24:19.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Write a function to find the longest common prefix string amongst an array of strings.**

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

``` python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        strs.sort()
        start = 0
        while start < len(strs[0]) and strs[0][start] == strs[-1][start]:
            start += 1
        return strs[0][:start]
```
