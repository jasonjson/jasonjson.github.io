---
layout: post
title: Remove Element
date: 2015-10-21 02:16:55.000000000 -04:00
categories:
- Integer
author: Jason
---
<p><strong><em>Given an array and a value, remove all instances of that value in place and return the new length. The order of elements can be changed. It doesn't matter what you leave beyond the new length.</em></strong></p>


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
