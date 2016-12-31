---
layout: post
title: 3 Sum Closest
date: 2015-10-21 02:22:25.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465719181;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:125;}i:1;a:1:{s:2:"id";i:1224;}i:2;a:1:{s:2:"id";i:123;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        if (nums == null || nums.length < 3) return -1;
        
        Arrays.sort(nums);
        int n = nums.length;
        int result = nums[0] + nums[1] + nums[2];
        for (int i = 0; i + 2 < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int lo = i + 1, hi = n - 1;
            while (lo < hi) {
                if (lo > i + 1 && nums[lo] == nums[lo - 1]) {
                    lo++;
                    continue;
                } 
                if (hi < n - 1 && nums[hi] == nums[hi + 1]) {
                    hi--;
                    continue;
                }
                int sum = nums[i] + nums[lo] + nums[hi];
                if (sum == target) {
                    return target;
                } else if (sum < target) {
                    lo++;
                } else {
                    hi--;
                }
                if (Math.abs(result - target) > Math.abs(sum - target)) {
                    result = sum;
                }
            }
        }
        return result;
    }
}
</pre>
<p>[/expand]</p>
