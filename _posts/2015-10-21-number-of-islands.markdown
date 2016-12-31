---
layout: post
title: Number of Islands
date: 2015-10-21 03:02:22.000000000 -04:00
type: post
published: true
status: publish
categories:
- DFS Backtracking
- Matrix
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467531727;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:302;}i:1;a:1:{s:2:"id";i:380;}i:2;a:1:{s:2:"id";i:1903;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a boolean 2D matrix, find the number of islands.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public int numIslands(boolean[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        int row = grid.length, col = grid[0].length;
        
        int count = 0;
        for (int i = 0; i < row; i ++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j]) {
                    count ++;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }
    
    public void dfs(boolean[][] grid, int i, int j) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || !grid[i][j]) return;
        grid[i][j] = false;
        dfs(grid, i - 1, j);
        dfs(grid, i + 1, j);
        dfs(grid, i, j - 1);
        dfs(grid, i, j + 1);
    }
}
</pre>
<p>[/expand]</p>
