---
layout: post
title: Compare Version Numbers
date: 2015-11-05 14:31:17.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Compare two version numbers version1 and version2.<br />

If version1 > version2 return 1, if version1 &lt; version2 return -1, otherwise return 0.<br />
You may assume that the version strings are non-empty and contain only digits and the . character.<br />
The . character does not represent a decimal point and is used to separate number sequences.<br />
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.</em></strong></p>
``` java
public class Solution {
    public int compareVersion(String version1, String version2) {
        int i = 0, j = 0;
        while (i < version1.length() || j < version2.length()) {
            int temp1 = 0, temp2 = 0;
            while (i < version1.length() && version1.charAt(i) != '.') {
                temp1 = temp1 * 10 + (version1.charAt(i++) - '0');
            }
            while (j < version2.length() && version2.charAt(j) != '.') {
                temp2 = temp2 * 10 + (version2.charAt(j++) - '0');
            }
            if (temp1 > temp2) {
                return 1;
            } else if (temp1 < temp2) {
                return -1;
            } else {
                i ++;
                j ++;
            }
        }
        return 0;
    }
}
```
