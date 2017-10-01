---
layout: post
title: Majority Number
date: 2015-10-21 02:40:10.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
- Integer
author: Jason
---
<p>**<em>Given an array of size n, find the majority element. The majority element is the element that appears more than $\floor</em> {n/2}$ times***</p>

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
