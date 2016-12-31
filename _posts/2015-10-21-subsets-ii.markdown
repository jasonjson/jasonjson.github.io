---
layout: post
title: Subsets II
date: 2015-10-21 03:37:09.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465736128;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:319;}i:1;a:1:{s:2:"id";i:323;}i:2;a:1:{s:2:"id";i:536;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a list of numbers that may has duplicate numbers, return all possible subsets</em></strong><br />
[expand title="code"]</p>
<pre>
class Solution {
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    public ArrayList<ArrayList<integer>> subsetsWithDup(ArrayList<integer> S) {
        // write your code here
        ArrayList<ArrayList<integer>> result = new ArrayList<ArrayList<integer>>();
        if (S == null || S.size() == 0) return result;
        
        Collections.sort(S);//remember to sort!!
        ArrayList<integer> list = new ArrayList<integer>();
        dfs(S, 0, list, result);
        return result;
    }
    
    public void dfs(ArrayList<integer> S, int start, ArrayList<integer> list, ArrayList<ArrayList<integer>> result) {
        result.add(new ArrayList<integer>(list));
        for (int i = start; i < S.size(); i++) {
            if (i > start && S.get(i) == S.get(i-1)) {
                continue;
                //jump i if it is the same with previous
                //i > start not i > 0, important!! same mistakes as in permutations problems
            }
            list.add(S.get(i));
            dfs(S, i + 1, list, result);
            list.remove(list.size() - 1);
        }
    }
}
</integer></integer></integer></integer></integer></integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
