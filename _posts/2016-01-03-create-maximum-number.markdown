---
layout: post
title: Create Maximum Number
date: 2016-01-03 19:08:09.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469115672;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:443;}i:1;a:1:{s:2:"id";i:200;}i:2;a:1:{s:2:"id";i:1038;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k &lt;= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int[] maxNumber(int[] nums1, int[] nums2, int k) {
        int[] result = new int[k];
        for (int i = Math.max(0, k - nums2.length); i <= nums1.length && i <= k; i++) {
            int[] candidate = merge(maxArr(nums1, i), maxArr(nums2, k - i), k);
            if (greater(candidate, 0, result, 0)) {
                result = candidate;
            }
        }
        return result;
    }
    
    public int[] maxArr(int[] nums, int k) {
        int[] result = new int[k];
        for (int i = 0, j = 0; i < nums.length; i++) {
            while (nums.length - i + j > k && j > 0 && result[j - 1] < nums[i]) {
                j--;
            }
            if (j < k) {
                result[j++] = nums[i];
            }
        }
        return result;
    }
    
    public boolean greater(int[] nums1, int i, int[] nums2, int j) {
        while (i < nums1.length && j < nums2.length && nums1[i] == nums2[j]) {
            i++;
            j++;
        }
        return j == nums2.length || (i < nums1.length && nums1[i] > nums2[j]);
    }
    public int[] merge(int[] nums1, int[] nums2, int k) {
        int[] result = new int[k];
        for (int i = 0, j = 0, l = 0; l < k; l++) {
            result[l] = greater(nums1, i, nums2, j) ? nums1[i++] : nums2[j++];
        }
        return result;
    }
}
</pre>
<p>[/expand]</p>
