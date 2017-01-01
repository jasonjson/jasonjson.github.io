---
layout: post
title: Median of unsorted array
date: 2015-10-21 02:25:36.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465046747;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1073;}i:1;a:1:{s:2:"id";i:143;}i:2;a:1:{s:2:"id";i:145;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a unsorted array with integers, find the median of it. A median is the middle number of the array after it is sorted. If there are even numbers in the array, return the N/2 th number after sorted.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param nums: A list of integers.
     * @return: An integer denotes the middle number of the array.
     */
    public int median(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return -1;
        
        return helper(nums, 0, nums.length - 1, (nums.length + 1) / 2);
    }
    
    public int helper(int[] nums, int start, int end, int k) {
        int lo = start, hi = end, pivot = end;
        while (lo <= hi) {
            while (lo <= hi && nums[lo] < nums[pivot]) lo ++;
            while (lo <= hi && nums[hi] >= nums[pivot]) hi --;
            if (lo < hi) {
                swap(nums, lo, hi);
            }
        }
        swap(nums, lo, pivot);
        if (lo + 1 == k) {
            return nums[lo];
        } else if (lo + 1 > k) {
            return helper(nums, start, lo - 1, k);
        } else {
            return helper(nums, lo + 1, end, k);
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
