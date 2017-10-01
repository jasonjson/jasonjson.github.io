---
layout: post
title: Subarray Sum
date: 2015-10-21 02:17:19.000000000 -04:00
tags:
- Leetcode
categories:
- Integer
- Subarray
author: Jason
---
<p><strong><em>Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.</em></strong></p>


``` java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number 
     *          and the index of the last number
     */
    public ArrayList<Integer> subarraySum(int[] nums) {
        // write your code here
        ArrayList<Integer> result = new ArrayList<Integer>();
        if (nums == null || nums.length == 0) return result;
        
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        map.put(0, -1);//must consider the possibility that sum is zero already
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (map.containsKey(sum)) {
                result.add(map.get(sum) + 1);
                result.add(i);
                return result;
            } else {
                map.put(sum, i);
            }
        }
        return result;
    }
}
```
