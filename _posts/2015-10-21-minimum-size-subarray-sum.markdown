---
layout: post
title: Minimum Size Subarray Sum
date: 2015-10-21 14:31:53.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
- Subarray
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464218981;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:109;}i:1;a:1:{s:2:"id";i:105;}i:2;a:1:{s:2:"id";i:111;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum >= s. If there isn't one, return -1 instead.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param nums: an array of integers
     * @param s: an integer
     * @return: an integer representing the minimum size of subarray
     */
    public int minimumSize(int[] nums, int s) {
        if (nums == null || nums.length == 0) return -1;
        int start = 0, sum = 0, len = nums.length + 1;
        for (int i = start; i < nums.length; i++) {
            sum += nums[i];
            while (sum >= s) {
                len = Math.min(len, i - start + 1);
                sum -= nums[start++];//先从sum减去再increment start,不能弄反
                //不论减去后sum是正是负都没关系，已经记录了len
            }            
        }
        return len == nums.length + 1 ? -1 : len;
    }
}
</pre>
<p>[/expand]</p>
