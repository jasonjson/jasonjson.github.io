---
layout: post
title: 1088 - Confusing Number II
date: 2020-02-02
tags:
- Leetcode
categories:
- Integer
author: Jason
---
We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid. A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.) Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.

```python
class Solution:
    def confusingNumberII(self, N: int) -> int:
        num_dict = {0: 0, 1: 1, 6:9, 8:8, 9:6}
        valid_nums = [0, 1, 6, 8, 9]


        ret = [0]
        def helper(num, rotation, digit):
            ret[0] += num != rotation
            for n in valid_nums:
                if num * 10 + n > N:
                    break
                helper(num * 10 + n, num_dict[n] * digit + rotation, digit * 10)

        helper(1, 1, 10)
        helper(6, 9, 10)
        helper(9, 6, 10)
        helper(8, 8, 10)
        return ret[0]
```
