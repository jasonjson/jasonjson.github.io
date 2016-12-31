---
layout: post
title: Interleaving Positive and Negative Numbers
date: 2015-10-21 14:21:54.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1461632037;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:449;}i:1;a:1:{s:2:"id";i:109;}i:2;a:1:{s:2:"id";i:1069;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
class Solution {
    public void rerange(int[] A) {
        if (A == null || A.length == 0) return;
        int negCnt = 0, posCnt = 0;
        for (int n : A) {
            if (n > 0) {
                posCnt ++;
            } else {
                negCnt ++;
            }
        }//put negative or positive number first
        int pos = 0, neg = 1;
        if (posCnt < negCnt) {
            pos = 1;
            neg = 0;
        }
        //quick sort
        while (pos < A.length && neg < A.length) {
            while (pos < A.length && A[pos] > 0) {
                pos += 2;
            }
            while (neg < A.length && A[neg] < 0) {
                neg += 2;
            }
            if (pos < A.length && neg < A.length) {
                swap(A, pos, neg);
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
