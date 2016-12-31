---
layout: post
title: First Missing Positive
date: 2015-10-21 02:20:34.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"a599774267db1d96621d24fcb8ef991e";a:2:{s:7:"expires";i:1462847339;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1073;}i:1;a:1:{s:2:"id";i:141;}i:2;a:1:{s:2:"id";i:559;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an unsorted integer array, find the first missing positive integer.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public int firstMissingPositive(int[] nums) {
        if (nums == null || nums.length == 0) return 1;
        for (int i = 0; i < nums.length; i++) {
            while (nums[i] > 0 && nums[i] - 1 < nums.length && nums[nums[i] - 1] != nums[i]) {
                swap(nums, nums[i] - 1, i);//把一个positive int 放在应在在位置上
            //while loop, not if, we keep swapping
            }
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] - 1 != i) {
                return i + 1;
            }
        }
        return nums.length + 1;
    }
    public void swap(int[] nums, int a, int b) {
        int temp = nums[b];
        nums[b] = nums[a];
        nums[a] = temp;
    }
}
</pre>
<p>[/expand]</p>
