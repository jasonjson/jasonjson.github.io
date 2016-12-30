---
layout: post
title: Find the Missing Number
date: 2015-10-21 13:02:42.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464778091;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:109;}i:1;a:1:{s:2:"id";i:1224;}i:2;a:1:{s:2:"id";i:1758;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array contains N numbers of 0 .. N, find which number doesn't exist in the array.</em></strong></p>
<p>[expand title="pigeon and cage"]</p>
<pre>
public class Solution {
    public int missingNumber(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int count = 0;
            for (int n : nums) {
                if (n <= mid) {
                    count ++;
                }
            }
            if (count == mid + 1) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**    
     * @param nums: an array of integers
     * @return: an integer
     */
    public int findMissing(int[] nums) {
        // write your code here
        int x1 = 0;
        for (int n : nums) {
            x1 ^= n;
        }        
        int x2 = 0;
        for (int i = 0; i <= nums.length; i++) {
            x2 ^= i;
        }
        return x1 ^ x2;
    }
    public int findMissing(int[] nums) {
        // write your code here
        bucketSort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) {
                return i;
            }
        }
        return nums.length;
    }
    //bucket sort
    public void bucketSort(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            while (nums[i] != i) {
                if (nums[i] == nums.length) {
                    break;
                } //nums[nums.length] out of bounds
                int nextNum = nums[nums[i]];
                nums[nums[i]] = nums[i];
                nums[i] = nextNum;
            }
        }
    }
}
</pre>
<p>[/expand]</p>
