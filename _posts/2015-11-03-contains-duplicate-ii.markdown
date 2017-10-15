---
layout: post
title: 219 - Contains Duplicate II
date: 2015-11-03 15:39:36.000000000 -05:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.**


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

``` python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if not nums:
            return False

        num_map = {}
        for i, num in enumerate(nums):
            if num in num_map and i - num_map[num] <= k:
                return True
            num_map[num] = i
        return False
```
