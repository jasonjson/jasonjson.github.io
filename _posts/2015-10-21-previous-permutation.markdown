---
layout: post
title: Previous Permutation
date: 2015-10-21 03:39:59.000000000 -04:00
tags: algorithm
categories:
- Permutation
author: Jason
---
<p><strong><em>Given a list of integers, which denote a permutation. Find the previous permutation in ascending order.</em></strong></p>


``` java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers that's previous permuation
     */
    public ArrayList<integer> previousPermuation(ArrayList<integer> nums) {
        if (nums == null || nums.size() == 0) return nums; 
        int n = nums.size();
        int i = n - 2;
        for (; i >= 0; i --) {
            if (nums.get(i) > nums.get(i+1)) {
                break;//from right to left find the first element violating decreasing order
            }//与next permutation正好相反,取值注意是ArrayList,不是Array
        }
        
        if (i != -1) {
            for (int k = n - 1; k > i; k --) {
                if (nums.get(k) < nums.get(i)) {
                    Collections.swap(nums, i, k);
                    break;
                }
            }
        }        
        int lo = left + 1, hi = n - 1;
        while (lo <= hi) {
            Collections.swap(nums, lo, hi);
            lo ++;
            hi --;
        }
        return nums;
    }
}
```
