---
layout: post
title: Combination Sum II
date: 2015-10-21 03:41:59.000000000 -04:00
type: post
published: true
status: publish
categories:
- DFS Backtracking
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"aa6ef5221cee22fc9dc7137e1b0f67d7";a:2:{s:7:"expires";i:1466826303;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:337;}i:1;a:1:{s:2:"id";i:1302;}i:2;a:1:{s:2:"id";i:2071;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. Each number in C may only be used once in the combination.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public List<List<integer>> combinationSum2(int[] num, int target) {
        List<List<integer>> result = new ArrayList<List<integer>>();
        if (num == null || num.length == 0) return result;
        
        Arrays.sort(num);
        helper(num, 0, target, new ArrayList<integer>(), result);
        return result;
    }
    
    public void helper (int[] num, int start, int remain, List<integer> list, List<List<integer>> result) {
        if (remain == 0) {
            result.add(new ArrayList<integer>(list));
            return;
        }
        for (int i = start; i < num.length; i++) {
            if (i > start && num[i] == num[i - 1]) continue;
            if (remain - num[i] >= 0) {
                list.add(num[i]);
                helper(num, i + 1, remain - num[i], list, result);
                list.remove(list.size() - 1);
            }
        }
    }
}
</integer></integer></integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
