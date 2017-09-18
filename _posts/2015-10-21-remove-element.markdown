---
layout: post
title: Remove Element
date: 2015-10-21 02:16:55.000000000 -04:00
tags:
- Algorithm
categories:
- Array
author: Jason
---
**Given an array and a value, remove all instances of that value in place and return the new length. The order of elements can be changed. It doesn't matter what you leave beyond the new length.**


``` java
public class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        for(int n : nums){
            if(n != val){
                //if n != val, we increment i
                nums[i++] = n;
            }
            //if n==val, we don't increment i, and nums[i] will be overwritten by n
        }
        return i;
    }
}
```

``` python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if not nums:
            return 0

        index = 0
        for num in nums:
            if num != val:
                nums[index] = num
                index += 1
        return index
```
