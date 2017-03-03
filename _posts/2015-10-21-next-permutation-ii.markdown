---
layout: post
title: Next Permutation
date: 2015-10-21 14:33:08.000000000 -04:00
tags: algorithm
categories:
- Permutation
author: Jason
---
<p><strong><em>Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers. If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).</em></strong></p>


``` java
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: return nothing (void), do not return anything, modify nums in-place instead
     */
    public void nextPermutation(int[] nums) {
        if (nums == null || nums.length == 0) return;
        
        int left = nums.length - 2;
        for (; left >= 0; left--) {
            if (nums[left] < nums[left + 1]) {
                break;
            }
        }
        
        if (left != -1) {
            int right = nums.length - 1;
            for (; right > left; right --) {
                if (nums[right] > nums[left]) {
                    break;
                }
            }
            swap(nums, left, right);
        }
        
        int lo = left + 1, hi = n - 1;
        while (lo <= hi) {
            swap(nums, lo, hi);
            lo ++;
            hi --;
        }//you have changes the high digit, now need to reverse low digits to make sure it's the next permutation, 一直要换到尾巴，不是仅仅换到right
        }
    }
    
    public void swap(int[] nums, int i , int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```
