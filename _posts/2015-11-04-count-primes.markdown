---
layout: post
title: 204 - Count Primes
date: 2015-11-04 14:55:54.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Count the number of prime numbers less than a non-negative number, n.**


``` java
public class Solution {
    public int countPrimes(int n) {
        if (n <= 2) return 0;
        int count = 0;
        boolean[] isPrime = new boolean[n];
        Arrays.fill(isPrime, true);先假定每个数都是prime然后去掉不是的
        isPrime[0] = false;
        isPrime[1] = false;
        for (int i = 2; i * i < n; i++) {
            if (isPrime[i]) {
                for (int j = 2; j * i < n; j++) {
                    isPrime[j * i] = false;
                }
            }
        }
        for (boolean i : isPrime) {
            if (i) {
                count ++;
            }
        }
        return count;
    }
}
```

``` python
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in xrange(2, n):
            if is_prime[i]:
                j = 2
                while i * j < n:
                    is_prime[i * j] = False
                    j += 1
        return sum([1 for i in is_prime if i])
```
