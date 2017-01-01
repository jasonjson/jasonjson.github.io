---
layout: post
title: Permutations
date: 2015-10-21 03:37:39.000000000 -04:00
type: post
published: true
status: publish
categories:
- DFS Backtracking
- Permutation
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463977550;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:327;}i:1;a:1:{s:2:"id";i:321;}i:2;a:1:{s:2:"id";i:319;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a list of numbers, return all possible permutations.</em></strong><br />
[expand title="code"]</p>
<pre>
class Solution {
    /**
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    public ArrayList<ArrayList<integer>> permute(ArrayList<integer> nums) {
        // write your code here
        ArrayList<ArrayList<integer>> result = new ArrayList<ArrayList<integer>>();
        if (nums == null || nums.size() == 0) return result;
        
        ArrayList<integer> list = new ArrayList<integer>();
        dfs(nums, list, result);
        return result;
    }
    
    public void dfs(ArrayList<integer> nums, ArrayList<integer> list, ArrayList<ArrayList<integer>> result) {
        if (list.size() == nums.size()) {
            result.add(new ArrayList<integer> (list));
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (list.contains(nums.get(i))) {
                continue;//if this number is already in the list, we continue
            }//assumes no duplicates in nums
            //对这种order matters的问题，不能increment start来处理问题
            list.add(nums.get(i));
            dfs(nums, list, result);
            list.remove(list.size() - 1);
        }
    }
}
</integer></integer></integer></integer></integer></integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
