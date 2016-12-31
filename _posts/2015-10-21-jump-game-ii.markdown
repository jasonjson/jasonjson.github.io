---
layout: post
title: Jump Game II
date: 2015-10-21 21:02:23.000000000 -04:00
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
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1454623300;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:105;}i:1;a:1:{s:2:"id";i:388;}i:2;a:1:{s:2:"id";i:1758;}}}}
  _inbound_impressions_count: '0'
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps.</em></strong></p>
<p>[expand title = "greedy"]</p>
<pre>
public class Solution {
    //The main idea is based on greedy. Let's say the range of the current jump is [curBegin, curEnd], curFarthest is the farthest point that all points in [curBegin, curEnd] can reach. Once the current point exceeds curEnd, then trigger another jump, and set the new curEnd with curFarthest, then keep the above steps, as the following:
    public int jump(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        
        int rightmost = 0, end = 0, count = 0;
        for (int i = 0; i < nums.length - 1; i++) {//!!nums.length - 1, when we are at the last index, we are finished. We don't need to consider the value at last index
            rightmost = Math.max(rightmost, nums[i] + i);
            if (i == end) {
                count ++;
                end = rightmost;
                if (end >= nums.length - 1) {
                    break;
                }
            }
        }
        return count;
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param A: A list of lists of integers
     * @return: An integer
     */
    public int jump(int[] A) {
        if (A == null || A.length == 0) return 0;
        
        int end = A.length - 1, min_index = end, count = 0;
        while (end > 0) {//end can't be zero, since min_index can't be negative
            for (int i = end - 1; i >= 0; i--) {
                if (A[i] >= end - i) {
                    min_index = i;
                }
            }
            if (min_index < end) {
                //min_index must be strictly smaller than end
                count ++;
                end = min_index;
            } else {
                return -1;
            }
        }
        return count;
    }
}
</pre>
<p>[/expand]</p>
