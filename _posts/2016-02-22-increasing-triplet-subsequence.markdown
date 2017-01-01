---
layout: post
title: Increasing Triplet Subsequence
date: 2016-02-22 23:25:30.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468608485;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:423;}i:1;a:1:{s:2:"id";i:2047;}i:2;a:1:{s:2:"id";i:1124;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.</em></strong></p>
<p>[expand title="DP, O(n^2) time"]</p>
<pre>
public class Solution {
    public boolean increasingTriplet(int[] nums) {
        if (nums == null || nums.length == 0) return false;
        
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = 1; i < n; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
                if (dp[i] >= 3) {
                    return true;
                }
            }
        }
        return false;
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title = "O(n)"]</p>
<pre>
public class Solution {
    public boolean increasingTriplet(int[] nums) {
        if (nums == null || nums.length == 0) return false;
        
        int min = Integer.MAX_VALUE, secondMin = Integer.MAX_VALUE;
        for (int num : nums) {
            if (num <= min) {
                min = num;//we need to include "=" here, otherwise secondMin might get updated when num == min
            } else if (num < secondMin) {
                secondMin = num;
            } else if (num > secondMin) {
                return true;
            }
        }
        return false;
    }
}
</pre>
<p>[/expand]</p>
