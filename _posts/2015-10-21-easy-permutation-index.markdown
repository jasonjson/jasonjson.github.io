---
layout: post
title: Permutation index
date: 2015-10-21 03:38:04.000000000 -04:00
tags: algorithm
categories:
- DFS Backtracking
- Permutation
author: Jason
---
<p><strong><em>Given a permutation which contains no repeated number, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.</em></strong></p>

<a href="http://algorithm.yuanbin.me/zh-cn/exhaustive_search/permutation_index.html">See explanations here</a></p>

``` java
public class Solution {
    /**
     * @param A an integer array
     * @return a long integer
     */
    public long permutationIndex(int[] A) {
        if (A.length == 0 || A == null) return 0;
        
        long index = 1, factor = 1;
        for (int i = A.length - 1; i >= 0; i--) {
            //从右边开始只是为了便于计算factorial
            int rank = 0;
            for (int j = i + 1; j < A.length; j++) {
                if (A[i] > A[j]) rank ++;
            }//找到i右边比A[i]小的数,从而计算把A[i]与之互换可能产生的index更小的permutation,
            index += rank * factor;
            factor *= A.length - i;
        }
        return index;
    }
}
```
