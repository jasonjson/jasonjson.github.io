---
layout: post
title: Move Zeroes
date: 2015-10-28 13:19:18.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
- Two Pointers
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464078654;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:119;}i:1;a:1:{s:2:"id";i:2006;}i:2;a:1:{s:2:"id";i:1578;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements. For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0]. Note: You must do this in-place without making a copy of the array. Minimize the total number of operations.</em></strong></p>
<p>[expand title="code1"]</p>
<pre>
public class Solution {
    public void moveZeroes(int[] nums) {
        if (nums == null || nums.length == 0) return;
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                int temp = nums[index];
                nums[index++] = nums[i];
                nums[i] = temp;
            }
        }
    }
}
</pre>
<p>[/expand]<br />
[expand title="code2"]</p>
<pre>
public class Solution {
    public void moveZeroes(int[] nums) {
        if (nums == null || nums.length == 0) return;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                int j = i + 1;
                while (j < nums.length) {
                    if (nums[j] != 0) {
                        break;
                    } else {
                        j ++;
                    }
                }
                if (j < nums.length) {
                    swap(nums, i, j);
                }
            }
        }
    }
    
    public void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}
</pre>
<p>[/expand]</p>
