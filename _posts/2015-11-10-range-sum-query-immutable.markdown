---
layout: post
title: Range Sum Query - Immutable
date: 2015-11-10 09:14:36.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469177352;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:2006;}i:1;a:1:{s:2:"id";i:109;}i:2;a:1:{s:2:"id";i:421;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class NumArray {
    int[] sums;
    public NumArray(int[] nums) {
        sums = new int[nums.length + 1];
        for (int i = 1; i <= nums.length; i++) {
            sums[i] = sums[i - 1] + nums[i - 1];
        }
    }

    public int sumRange(int i, int j) {
        return sums[j + 1] - sums[i];
    }
}
</pre>
<p>[/expand]</p>
