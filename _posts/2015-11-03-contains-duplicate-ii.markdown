---
layout: post
title: Contains Duplicate II
date: 2015-11-03 15:39:36.000000000 -05:00
tags: algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.</em></strong></p>


``` java
public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i< nums.length; i++){
            if ((map.containsKey(nums[i]) && (i - map.get(nums[i])) <= k)) {
                return true;
            }else{
                map.put(nums[i],i);
            }
        }
        return false;
    }
}
```
