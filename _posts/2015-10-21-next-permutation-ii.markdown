---
layout: post
title: Next Permutation
date: 2015-10-21 14:33:08.000000000 -04:00
type: post
published: true
status: publish
categories:
- Permutation
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467203699;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:331;}i:1;a:1:{s:2:"id";i:139;}i:2;a:1:{s:2:"id";i:1073;}}}}
  _inbound_impressions_count: '0'
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers. If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: return nothing (void), do not return anything, modify nums in-place instead
     */
    public void nextPermutation(int[] nums) {
        if (nums == null || nums.length == 0) return;
        
        int left = nums.length - 2;
        for (; left >= 0; left--) {
            if (nums[left] < nums[left + 1]) {
                break;
            }
        }
        
        if (left != -1) {
            int right = nums.length - 1;
            for (; right > left; right --) {
                if (nums[right] > nums[left]) {
                    break;
                }
            }
            swap(nums, left, right);
        }
        
        int lo = left + 1, hi = n - 1;
        while (lo <= hi) {
            swap(nums, lo, hi);
            lo ++;
            hi --;
        }//you have changes the high digit, now need to reverse low digits to make sure it's the next permutation, 一直要换到尾巴，不是仅仅换到right
        }
    }
    
    public void swap(int[] nums, int i , int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
</pre>
<p>[/expand]</p>
