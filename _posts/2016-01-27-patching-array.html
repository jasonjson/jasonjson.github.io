---
layout: post
title: Patching Array
date: 2016-01-27 14:15:01.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467185232;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:105;}i:1;a:1:{s:2:"id";i:121;}i:2;a:1:{s:2:"id";i:2006;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.</em></strong></p>
<p>[expand title="code1"]</p>
<pre>
//Let miss be the smallest sum in [1,n] that we might be missing. Meaning we already know we can build all sums in [1,miss). Then if we have a number num <= miss in the given array, we can add it to those smaller sums to build all sums in [1,miss+num). If we don't, then we must add such a number to the array, and it's best to add miss itself, to maximize the reach.
public class Solution {
    public int minPatches(int[] nums, int n) {
        long miss = 1;
        int result = 0, i = 0;
        while (miss <= n) {
            if (i < nums.length && nums[i] <= miss) {
                miss += nums[i++];
            } else {
                miss += miss;
                result ++;
            }
        }
        return result;
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title="code2"]</p>
<pre>
public class Solution {
    public int minPatches(int[] nums, int n) {
        if (nums == null || nums.length == 0) return 0;

        HashMap<Integer, Integer> map = new HashMap<>();
        helper(nums, 0, 0, map);
        List<integer> missing = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (!map.containsKey(i)) {
                missing.add(i);
            }
        }
        int result = 0;
        for (int miss : missing) {
            if (!map.containsKey(miss)) {
                result++;
                List<integer> elements = new ArrayList<>();
                elements.addAll(map.keySet());
                for (int key : elements) {
                    map.put(key + miss, 1);
                }
            }
        }
        return result;
    }

    public void helper(int[] nums, int start, int sum, HashMap<Integer, Integer>map) {
        if (sum != 0) {
            map.put(sum, 1);
        }
        for (int i = start; i < nums.length; i++) {
            helper(nums, i + 1, sum + nums[i], map);
        }
    }
}
</integer></integer></pre>
<p>[/expand]</p>
