---
layout: post
title: Subarray Sum
date: 2015-10-21 02:17:19.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
- Subarray
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465851950;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:107;}i:1;a:1:{s:2:"id";i:463;}i:2;a:1:{s:2:"id";i:466;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number 
     *          and the index of the last number
     */
    public ArrayList<integer> subarraySum(int[] nums) {
        // write your code here
        ArrayList<integer> result = new ArrayList<integer>();
        if (nums == null || nums.length == 0) return result;
        
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        map.put(0, -1);//must consider the possibility that sum is zero already
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (map.containsKey(sum)) {
                result.add(map.get(sum) + 1);
                result.add(i);
                return result;
            } else {
                map.put(sum, i);
            }
        }
        return result;
    }
}
</integer></integer></integer></pre>
<p>[/expand]</p>
