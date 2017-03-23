---
layout: post
title: Majority Element II
date: 2015-10-21 02:40:45.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
- Integer
author: Jason
---
<p><strong><em>Given an integer array of size n, find all elements that appear more than $\floor *{n/3}$ times. The algorithm should run in linear time and in O(1) space.</em></strong></p>


``` java
public class Solution {
    public List<integer> majorityElement(int[] nums) {
        if (nums == null) return null;
        List<integer> result = new ArrayList<integer>();
        int key1 = -1, key2 = -1, count1 = 0, count2 = 0;
        for (int n : nums) {
            if (count1 == 0) {
                key1 = n;
                count1 = 1;
            } else if (count2 == 0 && n != key1) {
                key2 = n;
                count2 = 1;
            } else {
                if (key1 == n) {
                    count1 ++;
                } else if (key2 == n) {
                    count2 ++;
                } else {
                    count1 --;
                    count2 --;
                }
            }
        }
        count1 = 0;
        count2 = 0;
        for (int n : nums) {
            if (key1 == n) {
                count1++;
            } else if (key2 == n) {
                count2++;
            }
        }
        if(count1 > nums.length / 3) result.add(key1);
        if(count2 > nums.length / 3) result.add(key2);
        return result;
    }
}
```
