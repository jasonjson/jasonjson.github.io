---
layout: post
title: Maximum Subarray II
date: 2015-10-21 12:51:32.000000000 -04:00
type: post
published: true
status: publish
categories:
- Dynamic Programming
- Subarray
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"c31158d1958e353b78ce3c647da78bc0";a:2:{s:7:"expires";i:1467460920;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:553;}i:1;a:1:{s:2:"id";i:414;}i:2;a:1:{s:2:"id";i:417;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array of integers, find two non-overlapping subarrays which have the largest sum. The number in each subarray should be contiguous. Return the largest sum.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: An integer denotes the sum of max two non-overlapping subarrays
     */
    public int maxTwoSubArrays(ArrayList<integer> nums) {
        if (nums == null || nums.size() == 0) return 0;
        
        int n = nums.size(), local = 0, max = Integer.MIN_VALUE;
        int[] left_max = new int[n];
        for (int i = 0; i < n - 1; i++) {
            local = Math.max(local, 0) + nums.get(i);//必须以nums.get(i)结尾
            if (i == 0) {
                left_max[i] = local;
            } else {
                left_max[i] = Math.max(left_max[i-1], local);
            }
        }
        
        local = 0;
        int right_max = Integer.MIN_VALUE;
        for (int i = n - 1; i > 0; i--) {
            local = Math.max(local, 0) + nums.get(i);
            right_max = Math.max(right_max, local);//不需要单独处理i == n - 1,但是right_max 得设为最小值,要保证right_max == local 当 i == n - 1 时
            max = Math.max(max, right_max + left_max[i - 1]);
        }
        return max;
    }
}
</integer></pre>
<p>[/expand]</p>
