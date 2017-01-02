---
layout: post
title: Count Primes
date: 2015-11-04 14:55:54.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Count the number of prime numbers less than a non-negative number, n.</em></strong></p>


<p>We start off with a table of n numbers. Let's look at the first number, 2. We know all multiples of 2 must not be primes, so we mark them off as non-primes. Then we look at the next number, 3. Similarly, all multiples of 3 such as 3 × 2 = 6, 3 × 3 = 9, ... must not be primes, so we mark them off as well. Now we look at the next number, 4, which was already marked off. What does this tell you? Should you mark off all multiples of 4 as well?</p>
<p>4 is not a prime because it is divisible by 2, which means all multiples of 4 must also be divisible by 2 and were already marked off. So we can skip 4 immediately and go to the next number, 5. Now, all multiples of 5 such as 5 × 2 = 10, 5 × 3 = 15, 5 × 4 = 20, 5 × 5 = 25, ... can be marked off. There is a slight optimization here, we do not need to start from 5 × 2 = 10. Where should we start marking off?</p>
<p>In fact, we can mark off multiples of 5 starting at 5 × 5 = 25, because 5 × 2 = 10 was already marked off by multiple of 2, similarly 5 × 3 = 15 was already marked off by multiple of 3. Therefore, if the current number is p, we can always mark off multiples of p starting at p2, then in increments of p: p2 + p, p2 + 2p, ... Now what should be the terminating loop condition?</p>
<p>It is easy to say that the terminating loop condition is p &lt; n, which is certainly correct but not efficient.</p>
<p>Yes, the terminating loop condition can be p &lt; √n, as all non-primes ≥ √n must have already been marked off. When the loop terminates, all the numbers in the table that are non-marked are prime.</p>
<p>The Sieve of Eratosthenes uses an extra O(n) memory and its runtime complexity is O(n log log n)</p>

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
