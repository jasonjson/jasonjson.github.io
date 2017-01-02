---
layout: post
title: Pascal's Triangle II
date: 2015-11-09 17:18:45.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given an index k, return the kth row of the Pascal's triangle.</em></strong></p>


``` java
public class Solution {
    public List<integer> getRow(int rowIndex) {
        List<integer> result = new ArrayList<integer>();
        result.add(1);
        for (int i = 1; i <= rowIndex; i++) {
            int size = result.size();
            for (int j = size - 1; j >= 1; j--) {
                result.set(j, result.get(j) + result.get(j - 1));
            }
            result.add(1);
        }
        return result;
    }
}
```
