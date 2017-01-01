---
layout: post
title: Remove Duplicates from Sorted Array
date: 2015-10-21 02:23:37.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465775942;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:133;}i:1;a:1:{s:2:"id";i:1124;}i:2;a:1:{s:2:"id";i:423;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length. Do not allocate extra space for another array, you must do this in place with constant memory. For example, Given input array nums = [1,1,2], Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param A: a array of integers
     * @return : return an integer
     */
    public int removeDuplicates(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return 0;
        int index = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i-1]) {
                index ++;
            }
            nums[index] = nums[i];
        }
        return index + 1;//长度比index多1
    }
}
</pre>
<p>[/expand]</p>
