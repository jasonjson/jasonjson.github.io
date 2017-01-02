---
layout: post
title: Pascal's Triangle
date: 2015-11-09 17:17:27.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given numRows, generate the first numRows of Pascal's triangle.</em></strong></p>


``` java
public class Solution {
    public List<List<integer>> generate(int numRows) {
        List<List<integer>> result = new ArrayList<List<integer>>();
        if (numRows <= 0) return result;
        for (int i = 1; i <= numRows; i++) {
            List<integer> list = new ArrayList<integer>();
            for (int j = 0; j < i; j++) {
                if (j == 0) {
                    list.add(1);
                } else if (j == i - 1) {
                    list.add(1);
                } else {
                    list.add(result.get(result.size() - 1).get(j - 1) + result.get(result.size() - 1).get(j));
                }
            }
            result.add(list);
        }
        return result;
    }
}
```
