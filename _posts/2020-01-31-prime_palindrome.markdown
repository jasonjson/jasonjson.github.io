---
layout: post
title: 866 - Prime_Palindrome
date: 2020-01-31
tags:
- Leetcode
categories:
- Integer
author: Jason
---
Find the smallest prime palindrome greater than or equal to N.

```python
class Solution:
    def primePalindrome(self, N: int) -> int:

        def is_prime(num):
            if num <= 2 or num % 2 == 0:
                return num == 2
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True

        if 8 <= N <= 11:
            return 11

        for x in range(10 ** (len(str(N)) // 2), 10 ** 5):
            new_x = int(str(x) + str(x)[-2::-1])
            if new_x >= N and is_prime(new_x):
                return new_x
        return -1
```
