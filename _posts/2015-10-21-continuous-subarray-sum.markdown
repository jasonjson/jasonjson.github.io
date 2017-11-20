---
layout: post
title: 402 - Continuous Subarray Sum
date: 2015-10-21 13:06:06.000000000 -04:00
tags:
- Lintcode
categories:
- Array
author: Jason
---
**Given an integer array, find a continuous subarray where the sum of numbers is the biggest. Your code should return the index of the first number and the index of the last number. (If their are duplicate answer, return anyone)**


``` java
public class Solution {
    /**
     * @param A an integer array
     * @return  A list of integers includes the index of the first number and the index of the last number
     */
    public ArrayList<Integer> continuousSubarraySum(int[] A) {
        // Write your code here
        ArrayList<Integer> result = new ArrayList<Integer>();
        if (A == null || A.length == 0) return result;

        int local_max = 0, global_max = Integer.MIN_VALUE;
        int start = 0;
        for (int i = 0; i < A.length; i++) {
            if (local_max <= 0) {
                start = i;
            }
            local_max = Math.max(A[i], local_max + A[i]);
            if (global_max < local_max) {
                global_max = local_max;
                result.clear();
                result.add(start);
                result.add(i);
            }
        }
        return result;
    }
}
```

``` python
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        # write your code here
        if not A:
            return

        start = local_max = 0
        global_max = - 2 * 31
        ret = []
        for i, num in enumerate(A):
            if local_max < 0:
                start = i
            local_max = max(num, local_max + num)
            if local_max > global_max:
                global_max = local_max
                ret = [start, i]
        return ret
```
