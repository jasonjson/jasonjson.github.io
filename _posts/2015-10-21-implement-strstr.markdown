---
layout: post
title: Implement strStr()
date: 2015-10-21 02:10:21.000000000 -04:00
categories:
- String
author: Jason
---
<p><strong><em>Implement strStr().Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.</em></strong></p>

<p><a href="https://www.youtube.com/watch?v=GTJr8OvyEVQ">read more</a><br />

``` java
public class Solution {
    public int strStr(String haystack, String needle) {
        int len1 = haystack.length(), len2 = needle.length();
        int[] key = new int[len2];
        for (int i = 1; i < len2; i++) {
            int j = key[i - 1];
            while (j != 0 && needle.charAt(i) != needle.charAt(j)) {
                j = key[j - 1];
            }
            key[i] = j + (needle.charAt(i) == needle.charAt(j) ? 1 : 0);//一定要括号起来！不然报错
        }
        int i = 0, j = 0;
        while (i < len2 && j < len1) {//i points to index in needle, j points to index at haystack
            if (i > 0 && needle.charAt(i) != haystack.charAt(j)) {
                i = key[i - 1];
            } else {
                i += (needle.charAt(i) == haystack.charAt(j) ? 1 : 0);
                j ++;
            }
        }
        return i == len2 ? j - len2 : -1;
    }
}
```

``` java
public class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0) return 0;

        int len1 = haystack.length(), len2 = needle.length();
        for (int i = 0; i + len2 - 1 < len1; i++) {
            for (int j = 0; j < len2; j++) {
                if (needle.charAt(j) != haystack.charAt(i + j)) {
                    break;
                }
                if (j == len2 - 1) {
                    return i;
                }
            }
        }
        return -1;
    }
}
```
