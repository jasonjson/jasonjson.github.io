---
layout: post
title: Find Minimum in Rotated Sorted Array
date: 2015-10-21 02:30:03.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
- Sorting
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463408440;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:163;}i:1;a:1:{s:2:"id";i:109;}i:2;a:1:{s:2:"id";i:1130;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Suppose a sorted array is rotated at some pivot unknown to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2). Find the minimum element.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public int findMin(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {//not <= 
            int mid = (lo + hi) / 2;
            if (nums[mid] < nums[hi]) {//右边有序,且右边的值都大于nums[mid]
                hi = mid;
            } else {//左边有序,且左边的值都大于nums[mid]
                lo = mid + 1;
            }
        }
        return nums[lo];
    }
}
</pre>
<p>[/expand]</p>
