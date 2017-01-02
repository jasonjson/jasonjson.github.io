---
layout: post
title: Unique Characters
date: 2015-10-21 03:35:07.000000000 -04:00
categories:
- String
author: Jason
---
<p><strong><em>Implement an algorithm to determine if a string has all unique characters.</em></strong><br />


``` java
public class Solution {
    /**
     * @param str: a string
     * @return: a boolean
     */
    public boolean isUnique(String str) {
        // write your code here
        if (str == null || str.length() == 0) return false;
        int[] existed = new int[256];
        
        for (int i = 0; i < str.length(); i++) {
            if (++existed[str.charAt(i)] > 1) return false;
        }
        return true;
    }
    //no extra space
    public boolean isUnique(String str) {
        // write your code here
        if (str == null || str.length() == 0) return false;
        
        for (int i = 0; i < str.length(); i++) {
            for (int j = i + 1; j < str.length(); j++) {
                if (str.charAt(i) == str.charAt(j)) {
                    return false;
                }
            }
        }
        return true;
    }
}
```
