---
layout: post
title: 119 - Pascal's Triangle II
date: 2015-11-09 17:18:45.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given an index k, return the kth row of the Pascal's triangle.**


``` java
public class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> result = new ArrayList<Integer>();
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

``` python
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """


        ret = [1]
        for i in range(rowIndex):
            for j in reversed(range(1, i + 1)):
                ret[j] += ret[j - 1]
            ret.append(1)
        return ret
```
