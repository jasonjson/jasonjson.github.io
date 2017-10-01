---
layout: post
title: Number Complement
date: 2017-04-30
tags:
- Leetcode
categories:
- Bit
author: Jason
---
**Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.**

```python
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        #convert number to binay string
        bin_str = "{0:b}".format(num)
        complement_str = "".join(["1" if digit == "0" else "0" for digit in bin_str])
        #convert binary string to num
        return int(complement_str, 2)
```

```python
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i = i << 1
        #eg: i = "10000", i - 1 = "1111"
        return (i - 1) ^ num
```
