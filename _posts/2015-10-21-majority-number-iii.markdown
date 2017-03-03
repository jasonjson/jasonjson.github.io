---
layout: post
title: Majority Number III
date: 2015-10-21 02:41:11.000000000 -04:00
tags: algorithm
categories:
- Brain teaser
- Integer
author: Jason
---
<p><strong><em>Given an array of integers and a number k, the majority number is the number that occurs more than 1/k of the size of the array.</em></strong></p>


``` java
public class Solution {
    public int majorityNumber(ArrayList<integer> nums, int k) {
        if (nums == null || nums.size() == 0 || k > nums.size()) return -1;
        //bug : nums.size() !!! not nums.size
        HashMap<Integer, Integer> map = new HashMap<Integer,Integer>();
        for (int n : nums) {
            if (map.containsKey(n)){
                map.put(n, map.get(n) + 1);
            } else if (map.size() < k) {
                map.put(n, 1);
            } else {
                ArrayList<integer> keys = new ArrayList<integer>();
                for (int key : map.keySet()) {
                    keys.add(key);
                }
                for (int key : keys) {
                    int val = map.get(key);
                    if (val == 1) {
                        map.remove(key);
                    } else {
                        map.put(key, val - 1);
                    }
                }
            }
        }
        List<integer> list = new ArrayList<>();
        for (int key : map.keySet()) {
            list.add(key);
        }
        map = new HashMap<>();
        for (int num : nums) {
            for (int key : list) {
                if (num == key) {
                    map.put(key, map.getOrDefault(key, 0) + 1);
                }
            }
        }//must count occurrences again   
        int count = 0, result = 0;
        for (int key : map.keySet()) {
            if (count < map.get(key)) {
                count = map.get(key);
                result = key;
            }
        }
        return result;
    }
}
```
