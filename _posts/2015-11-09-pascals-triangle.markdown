---
layout: post
title: 118 - Pascal's Triangle
date: 2015-11-09 17:17:27.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given numRows, generate the first numRows of Pascal's triangle.**


``` java
public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (numRows <= 0) return result;
        for (int i = 1; i <= numRows; i++) {
            List<Integer> list = new ArrayList<Integer>();
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

``` python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if not numRows:
            return []

        ret = []
        for i in range(1, numRows + 1):
            curr = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    curr.append(1)
                else:
                    curr.append(ret[-1][j] + ret[-1][j - 1])
            ret.append(curr)
        return ret
```
