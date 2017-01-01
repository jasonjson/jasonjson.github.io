---
layout: post
title: Combinations
date: 2015-10-21 03:41:06.000000000 -04:00
type: post
published: true
status: publish
categories:
- DFS Backtracking
tags: []
meta:
  _spost_short_title: ''
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465780789;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1302;}i:1;a:1:{s:2:"id";i:536;}i:2;a:1:{s:2:"id";i:443;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param n: Given the range of numbers
     * @param k: Given the numbers of combinations
     * @return: All the combinations of k numbers out of 1..n
     */
    public List<List<integer>> combine(int n, int k) {
        // write your code here
        List<List<integer>> result = new ArrayList<List<integer>>();
        if (n == 0 || k == 0) return result;
        List<integer> list = new ArrayList<integer>();
        
        combineUtil(n, k, 1, list, result);
        return result;
    }
    
    public void combineUtil(int n, int k, int start, List<integer> list, List<List<integer>> result) {
        if (list.size() == k) {
            result.add(new ArrayList<integer>(list));
            return; // for subset don't return
            //for permutation or a fixed size list, return so save time.
        }
        
        for (int i = start; i <= n; i++) {
            list.add(i);
            combineUtil(n, k, i + 1, list, result);
            list.remove(list.size() - 1);
        }
    }
}
</integer></integer></integer></integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
