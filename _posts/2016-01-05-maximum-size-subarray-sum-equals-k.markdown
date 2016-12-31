---
layout: post
title: Maximum Size Subarray Sum Equals k
date: 2016-01-05 12:18:15.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468839079;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:105;}i:1;a:1:{s:2:"id";i:421;}i:2;a:1:{s:2:"id";i:555;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        if (nums == null || nums.length == 0) return 0;
        
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int sum = 0, len = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (sum == k) {
                len = Math.max(len, i + 1);
            } else if (map.containsKey(sum - k)) {
                len = Math.max(len, i - map.get(sum - k));
            } 
            if (!map.containsKey(sum)) {
                map.put(sum, i);
            }
        }
        return len;
    }
}
</pre>
<p>[/expand]</p>
