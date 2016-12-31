---
layout: post
title: Continuous Subarray Sum II
date: 2015-10-21 13:06:45.000000000 -04:00
type: post
published: true
status: publish
categories:
- Subarray
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467372581;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:463;}i:1;a:1:{s:2:"id";i:105;}i:2;a:1:{s:2:"id";i:107;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an integer array, find a continuous rotate subarray where the sum of numbers is the biggest. Your code should return the index of the first number and the last number.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param A an integer array
     * @return  A list of integers includes the index of the first number and the index of the last number
     */
    public ArrayList<integer> continuousSubarraySumII(int[] A) {
        // Write your code here
        ArrayList<integer> result = new ArrayList<integer>();
        if (A == null || A.length == 0) return result;
        List<integer> max = helper(A, 1);
        List<integer> min = helper(A, -1);
        if (max.get(3) - min.get(2) > max.get(2)) {
            result.add(min.get(1) + 1);
            result.add(min.get(0) - 1);
        } else {
            result.add(max.get(0));
            result.add(max.get(1));
        }
        if (result.get(0) == A.length && result.get(1) == -1) {
            result.set(0, max.get(0));
            result.set(1, max.get(1));
        }
        return result;
    }
    
    public List<integer> helper(int[] A, int sign) {
        ArrayList<integer> result = new ArrayList<integer>();
        
        int local = 0, global = sign == 1 ? Integer.MIN_VALUE : Integer.MAX_VALUE;
        int start = 0, sum = 0;
        for (int i = 0; i < A.length; i++) {
            if (sign * local <= 0) {
                start = i;
                local = A[i];
            } else {
                local = local + A[i];
            }
            sum += A[i];
            if (sign * global < sign * local) {
                global = local;
                result.clear();
                result.addAll(Arrays.asList(start, i, global));
            }
        }
        result.add(sum);
        return result;
    }
}
</integer></integer></integer></integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
