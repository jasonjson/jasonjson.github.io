---
layout: post
title: Largest sibling
date: 2015-10-25 20:08:38.000000000 -04:00
categories:
- Integer
- Cloudera OA
author: Jason
---
<p><strong><em>Given a number, find the largest sibling</em></strong></p>

``` java
public class solution {
    public int largestSibling(int num) {
        char[] chars = String.valueOf(num).toCharArray();
        Arrays.sort(chars);
        long result = 0;
        for (int i = chars.length - 1; i >= 0; i --) {
            result = result * 10 + Character.getNumericValue(chars[i]);
        }
        if (result > Integer.MAX_VALUE) {
            return Integer.MAX_VALUE;
        } else {
            return (int)result;//cast long back to int!!!
        }
    }
}
```
