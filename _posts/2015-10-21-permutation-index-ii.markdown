---
layout: post
title: Permutation Index II
date: 2015-10-21 03:42:42.000000000 -04:00
tags: algorithm
categories:
- Permutation
author: Jason
---
<p><strong><em>Given a permutation which may contain repeated numbers, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.</em></strong></p>


``` java
public class Solution {
    public long permutationIndexII(int[] A) {
        if (A == null || A.length == 0) return 1;        
        long index = 1, factorial = 1;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = A.length - 1; i >= 0; i--) {
            map.put(A[i], map.getOrDefault(A[i], 0) + 1);
            int rank = 0;
            for (int j = i + 1; j < A.length; j ++) {
                if (A[i] > A[j]) {
                    rank ++;
                }
            }//divide by factorials of duplicate elements
            index += rank * factorial / dupPerm(map);            
            factorial *= A.length - i;
        }
        return index;
    }    
    public long dupPerm(HashMap<Integer, Integer> map) {
        long val = 1;
        for (int key : map.keySet()) {
            val *= fact(map.get(key));
        }
        return val;
    }
    public long fact(int n) {
        if (n == 0) return 1;
        long val = 1;
        for (int i = 2; i <= n; i++) {
            val *= i;
        }
        return val;
    }
}
```
