---
layout: post
title: Wiggle Sort
date: 2015-10-29 14:09:31.000000000 -04:00
type: post
published: true
status: publish
categories:
- Sorting
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469125241;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:423;}i:1;a:1:{s:2:"id";i:1386;}i:2;a:1:{s:2:"id";i:1038;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an unsorted array nums, reorder it in-place such that nums[0] &lt;= nums[1] >= nums[2] &lt;= nums[3].... For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public void wiggleSort(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            if ((i % 2 == 1 && nums[i] < nums[i - 1]) || (i % 2 == 0 && nums[i] > nums[i - 1])) {
                //当i是基数, 必须大于左右两边,当i是偶数，必须小于左右两边
                int tmp = nums[i];
                nums[i] = nums[i - 1];
                nums[i - 1] = tmp;
            }
        }
    }
}
</pre>
<p>[/expand]</p>
