---
layout: post
title: Subarray Sum II
date: 2015-10-21 02:18:11.000000000 -04:00
type: post
published: true
status: publish
categories:
- Subarray
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463840974;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:111;}i:1;a:1:{s:2:"id";i:1578;}i:2;a:1:{s:2:"id";i:105;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an integer array, find a subarray where the sum of numbers is between two given interval. Your code should return the number of possible answer.</em></strong></p>
<p>[expand title = "O(nlgn)"]</p>
<pre>
public class Solution {
    public int subarraySumII(int[] nums, int start, int end) {
        if (nums == null || nums.length == 0 || start > end) return 0;
        
        int[] sum = new int[nums.length];
        sum[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            sum[i] = sum[i - 1] + nums[i];
        }
        Arrays.sort(sum);
        int count = 0;
        for (int i = 0; i < sum.length; i++) {
            if (sum[i] >= start && sum[i] <= end) {
                count ++;
            }
            int left = sum[i] - end, right = sum[i] - start;
            // start <= sum[i] - sum[j] <= end
            // sum[i] - end <= sum[j] <= sum[i] - start;
            //找到满足这个条件的sum[j]的个数
            //找到左边比right大的最小数的index和右边比left小的最大数的index
            count += find(sum, right + 1) - find(sum, left);
        }
        return count;
    }
    public int find(int[] sum, int val) {
        int lo = 0, hi = sum.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (val == sum[mid]) {
                return mid;
            } else if (val < sum[mid]) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
</pre>
<p>[/expand]<br />
[expand title="O(n^2)"]</p>
<pre>
public class Solution {
    /**
     * @param A an integer array
     * @param start an integer
     * @param end an integer
     * @return the number of possible answer
     */
    public int subarraySumII(int[] A, int start, int end) {
        // Write your code here
        if (A == null) return -1;
        
        int count = 0;
        int[] sums = new int[A.length + 1];
        for (int i = 1; i <= A.length; i++) {
            sums[i] = sums[i-1] + A[i-1];
        }//这种问题都A.length + 1,必须考虑A[0]也可能满足条件
        //Arrays.sort(sums); no need to sort, we are trying every i, j
        for (int i = 0; i <= A.length; i++) {
            for (int j = i; j <= A.length; j++) {
                if (sums[j] - sums[i] >= start && sums[j] - sums[i] <= end){
                    count ++;
                }
            }
        }
        return count;
    }
}
</pre>
<p>[/expand]</p>
