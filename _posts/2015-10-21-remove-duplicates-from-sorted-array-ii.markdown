---
layout: post
title: Remove Duplicates from Sorted Array II
date: 2015-10-21 02:24:13.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468796752;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:131;}i:1;a:1:{s:2:"id";i:105;}i:2;a:1:{s:2:"id";i:1298;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Follow up for "Remove Duplicates":<br />
What if duplicates are allowed at most twice?</em></strong></p>
<p>[expand title="code1"]</p>
<pre>
public class Solution {
    /**
     * @param A: a array of integers
     * @return : return an integer
     */
    public int removeDuplicates(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return 0;
        
        int flag = 0, index = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1] && flag == 0) {
                index ++;
                flag = 1;
            } else if (nums[i] != nums[i-1]) {
                flag = 0;
                index ++;
            }
            nums[index] = nums[i];
        }
        return index + 1;
    }
}
</pre>
<p>[/expand]<br />
[expand title="code2"]</p>
<pre>
public class Solution {
    //hash map solution
    public int removeDuplicates(int[] nums) {
        int j = 0;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for ( int i = 0; i < nums.length; i++ ) {
            if(map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i]) + 1);
                if ( map.get(nums[i]) > 2 ) { continue; }
            }else{
                map.put(nums[i], 1);
            }
            nums[j++] = nums[i];
        }
        return j;
    }
</pre>
<p>[/expand]</p>
