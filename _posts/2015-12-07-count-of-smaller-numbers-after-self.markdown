---
layout: post
title: Count of Smaller Numbers After Self
date: 2015-12-07 18:21:09.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Sorting
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469250502;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:936;}i:1;a:1:{s:2:"id";i:499;}i:2;a:1:{s:2:"id";i:109;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].</em></strong></p>
<p>[expand title="binary search"]</p>
<pre>
public class Solution {
    public List<integer> countSmaller(int[] nums) {
        List<integer> result = new ArrayList<integer>();
        if (nums == null || nums.length == 0) return result;

        List<integer> sorted = new ArrayList<>();
        for (int i = nums.length - 1; i >= 0; i--) {
            int index = find(sorted, nums[i]);
            result.add(index);
            sorted.add(index,nums[i]);
        }
        Collections.reverse(result);//!!don't forget to reverse
        return result;
    }

    public int find(List<integer> sorted, int val) {
        //if (sorted.size() == 0) return 0; no need
        int lo = 0, hi = sorted.size() - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (sorted.get(mid) == val) {
                while (mid - 1 >= 0 && sorted.get(mid - 1) == val) {
                    mid--;
                }
                return mid;
            } else if (sorted.get(mid) < val) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }
}
</integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
