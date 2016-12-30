---
layout: post
title: Count of Range Sum
date: 2016-01-09 23:37:50.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469289532;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1578;}i:1;a:1:{s:2:"id";i:2071;}i:2;a:1:{s:2:"id";i:109;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive. Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.</em></strong></p>
<p>[expand title = "O(nlgn)"]</p>
<pre>
public class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        if (nums == null || nums.length == 0) return 0;
        
        long[] sum = new long[nums.length + 1];
        for (int i = 1; i <= nums.length; i++) {
            sum[i] = sum[i - 1] + nums[i - 1];
        }
        return helper(sum, 0, sum.length, lower, upper);
    }
    public int helper(long[] sum, int start, int end, int lower, int upper) {
        if (start + 1 >= end) return 0;
        int mid = (start + end) / 2;
        int result = helper(sum, start, mid, lower, upper) + helper(sum, mid, end, lower, upper);
        int k = mid, l = mid, r = mid;
        long[] cache = new long[end - start];
        for (int i = start, j = 0; i < mid; ++i, ++j) {
            while (k < end && sum[k] - sum[i] < lower) k++;
            while (l < end && sum[l] - sum[i] <= upper) l++;
            while (r < end && sum[r] < sum[i]) cache[j++] = sum[r++];
            cache[j] = sum[i];
            result += l - k;
        }
        System.arraycopy(cache, 0, sum, start, r - start);
        return result;
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title="O(n^2)"]</p>
<pre>
public class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        if (nums == null || nums.length == 0) return 0;
        
        int[] sum = new int[nums.length + 1];
        for (int i = 1; i <= nums.length; i++) {
            sum[i] = sum[i - 1] + nums[i - 1];
        }
        int count = 0;
        for (int i = 0; i + 1 <= nums.length; i++) {
            for (int j = i + 1; j <= nums.length; j++) {
                if (sum[j] - sum[i] >= lower && sum[j] - sum[i] <= upper) {
                    count ++;
                }
            }
        }
        return count;
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title = "O(n3)"]</p>
<pre>
public class Solution {
    public static void main(String[] args) {
        int[] nums = {-2, 5, -1};
        System.out.println(countRangeSum(nums, -2, 2));
    }
    public static int countRangeSum(int[] nums, int lower, int upper) {
        if (nums == null || nums.length == 0) return 0;

        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = i; j < nums.length; j++) {
                int sum = 0;
                for (int k = i; k <= j; k++) {
                    sum += nums[k];
                }
                if (sum >= lower && sum <= upper) {
                    count ++;
                }
            }

        }
        return count;
    }
}
</pre>
<p>[/expand]</p>
