---
layout: post
title: 169 - Majority Number
date: 2015-10-21 02:40:10.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
- Integer
author: Jason
---
**Given an array of size n, find the majority element. The majority element is the element that appears more than {n/2} times**


``` java
public class Solution {
    public int majorityElement(int[] nums) {
        int key = -1, count = 0;
        for (int n : nums) {
            if (count == 0) {
                key = n;
                count ++;
            } else {
                if (key == n) {
                    count ++;
                } else {
                    count --;
                }
            }
        }
        return key;
        //bug: return count
    }
}
```

``` python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = ret = 0
        for num in nums:
            if count == 0:
                ret = num
                count += 1
            else:
                count += 1 if num == ret else -1
        return ret
```
