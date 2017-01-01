---
layout: post
title: N-Queens II
date: 2015-10-21 13:24:37.000000000 -04:00
type: post
published: true
status: publish
categories:
- DFS Backtracking
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465354238;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:472;}i:1;a:1:{s:2:"id";i:1148;}i:2;a:1:{s:2:"id";i:380;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int totalNQueens(int n) {
        if (n <= 0) return 0;
        
        int[] result = new int[1];
        helper(n, new ArrayList<integer>(), result);
        return result[0];
    }
    
    public void helper(int n, List<integer> cols, int[] result) {
        if (cols.size() == n) {
            result[0] ++;
            return;
        }
        for (int i = 0; i < n; i++) {
            if (isValid(cols, i)) {
                cols.add(i);
                helper(n, cols, result);
                cols.remove(cols.size() - 1);
            }
        }
    }
    
    public boolean isValid(List<integer> cols, int col) {
        int row = cols.size();
        for (int i = 0; i < row; i++) {
            if (cols.get(i) == col || i + cols.get(i) == row + col || i - cols.get(i) == row - col) {
                return false;
            }
        }
        return true;
    }
}
</integer></integer></integer></pre>
<p>[/expand]</p>
