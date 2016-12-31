---
layout: post
title: Combination Sum
date: 2015-10-21 03:41:33.000000000 -04:00
type: post
published: true
status: publish
categories:
- DFS Backtracking
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1462824368;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:339;}i:1;a:1:{s:2:"id";i:1302;}i:2;a:1:{s:2:"id";i:536;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. The same repeated number may be chosen from C unlimited number of times.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public List<List<integer>> combinationSum(int[] candidates, int target) {
        List<List<integer>> result = new ArrayList<List<integer>>();
        if (candidates == null || candidates.length == 0) return result;
        List<integer> list = new ArrayList<integer>();
        
        Arrays.sort(candidates);
        helper(candidates, 0, target, list, result);
        return result;
    }
    
    public void helper(int[] candidates, int start, int gap, List<integer> list, List<List<integer>> result) {
        if (gap == 0) {
            result.add(new ArrayList<integer>(list));
            return;
        }        
        for (int i = start; i < candidates.length; i++) {
            if (i > start && candidate[i] == candidates[i - 1]) continue;
            if (gap - candidates[i] >= 0) {
                list.add(candidates[i]);
                helper(candidates, i, gap - candidates[i], list, result);
                list.remove(list.size() - 1);
            }
        }
    }
}
</integer></integer></integer></integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
