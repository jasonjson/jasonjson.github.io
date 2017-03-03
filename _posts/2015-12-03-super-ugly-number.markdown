---
layout: post
title: Super Ugly Number
date: 2015-12-03 21:42:33.000000000 -05:00
tags: algorithm
categories:
- Brain teaser
- Dynamic Programming
author: Jason
---
<p><strong><em>Write a program to find the nth super ugly number. Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.</em></strong></p>


``` java
public class Solution {//the same idea with ugly number
    public static int nthSuperUglyNumber(int n, int[] primes) {
        int[] indexes = new int[primes.length];
        int[] result = new int[n];
        result[0] = 1;
        for (int i = 1; i < n; i++) {
            result[i] = Integer.MAX_VALUE;
            for (int j = 0; j < indexes.length; j++) {
                result[i] = Math.min(result[i], result[indexes[j]] * primes[j]);
            }
            for (int j = 0; j < indexes.length; j++) {
                if (result[i] == result[indexes[j]] * primes[j]) {
                    indexes[j]++;
                }
            }
        }
        return result[n-1];
    }
}
```
