---
layout: post
title: Sliding Window Median
date: 2015-10-21 14:46:43.000000000 -04:00
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
<p><strong><em>Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array, find the median of the element inside the window at each moving. (If there are even numbers in the array, return the N/2-th number after sorting the element in the window. )</em></strong></p>


``` java
public class Solution {
    public ArrayList<integer> medianSlidingWindow(int[] nums, int k) {
        ArrayList<integer> result = new ArrayList<integer>();
        if (nums == null || nums.length == 0) return result;
        PriorityQueue<integer> max_heap = new PriorityQueue<integer>(10, Collections.reverseOrder());// 10 is initial capacity
        PriorityQueue<integer> min_heap = new PriorityQueue<integer>();
        for (int i = 0; i < nums.length; i++) {
            if (max_heap.isEmpty() || nums[i] < max_heap.peek()) {
                max_heap.add(nums[i]);
            } else {
                min_heap.add(nums[i]);
            }
            
            if (min_heap.size() > max_heap.size()) {
                max_heap.add(min_heap.poll());
            }
            if (max_heap.size() > min_heap.size() + 1) {
                min_heap.add(max_heap.poll());
            }
            if (i + 1 >= k) {
                result.add(max_heap.peek());
                int to_remove = nums[i - k + 1];
                if (to_remove <= max_heap.peek()) {
                    max_heap.remove(to_remove);
                } else {
                    min_heap.remove(to_remove);
                }
                if (min_heap.size() > max_heap.size()) {
                    max_heap.add(min_heap.poll());
                }
                if (max_heap.size() > min_heap.size() + 1) {
                    min_heap.add(max_heap.poll());
                }
            }
        }
        return result;
    }
}//http://blog.csdn.net/chen895281773/article/details/9533711
//http://jane4532.blogspot.com/2015/07/lintcode-sliding-window-median.html
```
