---
layout: post
title: Data Stream Median
date: 2015-10-27 12:42:16.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466608945;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:606;}i:1;a:1:{s:2:"id";i:443;}i:2;a:1:{s:2:"id";i:1138;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Numbers keep coming, return the median of numbers at every time a new number added.</em></strong></p>
<p>[expand title = "two heap, O(nlgn)"]</p>
<pre>
public class Solution {
    /**
     * @param nums: A list of integers.
     * @return: the median of numbers
     */
    public int[] medianII(int[] nums) {
        int[] result = new int[nums.length];
        
        PriorityQueue<integer> min = new PriorityQueue<integer>();
        PriorityQueue<integer> max = new PriorityQueue<integer>(10, Collections.reverseOrder());
        
        for (int i = 0; i < nums.length; i++) {
            if (max.isEmpty() || nums[i] < max.peek()) {
                max.offer(nums[i]);
            } else {
                min.offer(nums[i]);
            }
            if (min.size() > max.size()) {
                max.offer(min.poll());
            }
            if (max.size() > min.size() + 1) {
                min.offer(max.poll());
            }
            result[i] = max.peek();
        }
        return result;
    }
}
</integer></integer></integer></integer></pre>
<p>[/expand]<br />
[expand title="O(n^2)"]</p>
<pre>
public class Solution {
    /**
     * @param nums: A list of integers.
     * @return: the median of numbers
     */
    public int[] medianII(int[] nums) {
        // write your code here
        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            result[i] = helper(nums, 0, i, i / 2 + 1);
        }
        return result;
    }
        
    public int helper(int[] nums, int start, int end, int med) {
        int lo = start, hi = end, pivot = end;
        while (lo <= hi) {
            while (lo <= hi && nums[hi] >= nums[pivot]) hi --;
            while (lo <= hi && nums[lo] < nums[pivot]) lo ++;
            if (lo < hi) {
                swap(nums, lo, hi);
                lo ++;
                hi --;
            }
        }
        swap(nums, lo, pivot);
        if (med == lo + 1) {
            return nums[lo];
        } else if (med > lo + 1) {
            return helper(nums, lo + 1, end, med);
        } else {
            return helper(nums, start, lo - 1, med);
        }
    }
    public void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}
</pre>
<p>[/expand]</p>
