---
layout: post
title: House Robber II
date: 2015-11-03 18:28:31.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Dynamic Programming
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468771871;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:519;}i:1;a:1:{s:2:"id";i:1213;}i:2;a:1:{s:2:"id";i:1231;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.<br />
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    //Taking into account this circular constraint, either we rob the house at index 0, or the house at last index n. In order to reduce this problem to the simpler problem House Robber I, we need to remove the circular condition.
    //If we assume that the house at index 0 is not robbed, then we can compute the maximum robbed value using the same algorithm for the linear problem House Robber I.
    //In the same way, we compute the maximum robbed value by assuming that the house at last index n is not robbed.
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        if (n == 1) return nums[0];
        if (n == 2) return Math.max(nums[0], nums[1]);
        return Math.max(helper(Arrays.copyOfRange(nums, 0, nums.length-1)), helper(Arrays.copyOfRange(nums, 1, nums.length)));
    }
    
    public int helper(int[] nums) {
        int n = nums.length;
        nums[1] = Math.max(nums[0], nums[1]);
        for (int i = 2; i < n; i++) {
            nums[i] = Math.max(nums[i - 2] + nums[i], nums[i - 1]);
        }
        return nums[n-1];
    }
}
</pre>
<p>[/expand]</p>
