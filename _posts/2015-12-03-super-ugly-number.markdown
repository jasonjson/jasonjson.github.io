---
layout: post
title: 313 - Super Ugly Number
date: 2015-12-03 21:42:33.000000000 -05:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Write a program to find the nth super ugly number. Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.**


``` java
public class Solution {
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

``` python
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        primes_index = [0] * len(primes)
        num = [0] * n
        num[0] = 1
        for i in xrange(1, n):
            num[i] = min([num[primes_index[j]] * primes[j] for j in xrange(len(primes))])
            for k in xrange(len(primes)):
                if num[i] == num[primes_index[k]] * primes[k]:
                    primes_index[k] += 1

        return num[-1]
```
