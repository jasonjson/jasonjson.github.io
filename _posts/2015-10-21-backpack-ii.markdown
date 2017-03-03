---
layout: post
title: Backpack II
date: 2015-10-21 03:57:56.000000000 -04:00
tags: algorithm
categories:
- Dynamic Programming
author: Jason
---
<p><strong><em>Given n items with size Ai and value Vi, and a backpack with size m. What's the maximum value can you put into the backpack?</em></strong></p>


``` java
public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A & V: Given n items with size A[i] and value V[i]
     * @return: The maximum value
     */
    public int backPackII(int m, int[] A, int V[]) {
        // write your code here
        int[][] value = new int[A.length + 1][m + 1];
        
        for (int i = 1; i <= A.length; i++) {
            for (int j = 1; j <= m; j++) {
                if (j >= A[i - 1]) {
                    value[i][j] = Math.max(value[i-1][j-A[i-1]] + V[i-1], value[i-1][j]);
                } else {
                    value[i][j] = value[i-1][j];
                }
            }
        }
        return value[A.length][m];
    }
}
```
``` java
public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A & V: Given n items with size A[i] and value V[i]
     * @return: The maximum value
     */
    public int backPackII(int m, int[] A, int V[]) {
        int n = A.length;
        int[] total = new int[m+1];//we overwrite total each iteration
        for (int i = 0; i < n; i++) {
            for (int j = m; j >= 0; j--) {//j starts from m
                if (j == 0) {
                    total[j] = 0;
                } else if (j - A[i] >= 0) {
                    total[j] = Math.max(total[j - A[i]] + V[i], total[j]);
                }
            }
        }
        return total[m];
    }
}
```
