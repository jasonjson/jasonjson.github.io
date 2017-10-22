---
layout: post
title: 260 - Single Number III
date: 2015-10-21 02:34:47.000000000 -04:00
tags:
- Leetcode
categories:
- Bit
author: Jason
---
**Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.**

The two numbers that appear only once must differ at some bit, this is how we can distinguish between them. Otherwise, they will be one of the duplicate numbers. Let’s say the at the ith bit, the two desired numbers differ from each other. which means one number has bit i equaling: 0, the other number has bit i equaling 1. Thus, all the numbers can be partitioned into two groups according to their bits at location i. the first group consists of all numbers whose bits at i is 0. the second group consists of all numbers whose bits at i is 1. Notice that, if a duplicate number has bit i as 0, then, two copies of it will belong to the first group. Similarly, if a duplicate number has bit i as 1, then, two copies of it will belong to the second group. by XoRing all numbers in the first group, we can get the first number. by XoRing all numbers in the second group, we can get the second number.


``` java
public class Solution {
   public List<Integer> singleNumberIII(int[] A) {
        int xor = 0;
        for (int n : A) {
            xor ^= n;
        }
        xor &= -xor; // find the last none zero digit
        //1011 & -1011 = 1
        //101100 & -101100 = 100

        int x1 = 0, x2 = 0;
        for (int n : A) {
            if ((xor & n) == 0) {
                x1 ^= n;
            } else {
                x2 ^= n;
            }
        }
        return new ArrayList<Integer>(Arrays.asList(x1, x2));
    }
}
```

``` python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        xor = 0
        for num in nums:
            xor ^= num

        xor &= -xor
        x1 = x2 = 0
        for num in nums:
            if num & xor:
                x1 ^= num
            else:
                x2 ^= num
        return [x1, x2]
```
