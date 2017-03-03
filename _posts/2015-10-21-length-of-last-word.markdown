---
layout: post
title: Length of Last Word
date: 2015-10-21 02:15:44.000000000 -04:00
tags: algorithm
categories:
- String
author: Jason
---
<p><strong><em>Given a string s consists of upper/lower-case alphabets and empty space characters ' ',</p>

return the length of last word in the string.If the last word does not exist, return 0.</em></strong></p>

``` java
public class Solution {
    public static int lengthOfLastWord(String s) {
        if (s ==  null || s == " ") return 0;
        String[] arr = s.split(" ");
        int n = arr.length;
        if (n > 0) { 
            return (arr[n-1].length());
        } else {
            return 0;
        }
    }
    
    public static int lengthOfLastWord(String s) {
        if(s == null || s.length() == 0) return 0;
        
        int start = 0, end = s.length() - 1;
        while (end > 0 && s.charAt(end) == ' ') { 
            end --;
        }
        for (int i = 0; i <= end; i++) {
            if (s.charAt(i) == ' ') {
                start = i + 1;
            }
        }
        return end - start + 1;
    }
}
```
