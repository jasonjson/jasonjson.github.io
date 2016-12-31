---
layout: post
title: Sliding Window Median
date: 2015-10-21 14:46:43.000000000 -04:00
type: post
published: true
status: publish
categories:
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469167955;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:443;}i:1;a:1:{s:2:"id";i:1073;}i:2;a:1:{s:2:"id";i:2049;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array, find the median of the element inside the window at each moving. (If there are even numbers in the array, return the N/2-th number after sorting the element in the window. )</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</integer></integer></integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
