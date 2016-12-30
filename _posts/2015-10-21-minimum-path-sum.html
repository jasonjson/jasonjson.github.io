---
layout: post
title: Minimum Path Sum
date: 2015-10-21 12:24:23.000000000 -04:00
type: post
published: true
status: publish
categories:
- Matrix
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1452318734;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:347;}i:1;a:1:{s:2:"id";i:1148;}i:2;a:1:{s:2:"id";i:302;}}}}
  _inbound_impressions_count: '0'
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.</em></strong></p>
<p>[expand title="O(1)space"]</p>
<pre>
public class Solution {
    /**
     * @param grid: a list of lists of integers.
     * @return: An integer, minimizes the sum of all numbers along its path
     */
    public int minPathSum(int[][] grid) {
        // write your code here
        int row = grid.length, col = grid[0].length;
        if (grid == null || row == 0 || col == 0) return 0;
        
        for (int i = 0; i < row; i ++) {
            for (int j = 0; j < col; j ++) {
                if (i == 0 && j == 0) continue;
                else if (i == 0) {
                    grid[i][j] += grid[i][j-1];
                } else if (j == 0) {
                    grid[i][j] += grid[i-1][j];
                } else {
                    grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1]);
                }
            }
        }
        
        //after this, grid[i][j] denotes the smallest sum from [0][0] to [i][j],
        //since each time we find the smallest sum so far and add it to the current value at original grid[i][j]
        // 1 3 1     1 4 5
        // 1 5 1  => 2 7 6
        // 4 2 1     6 8 7 
        return grid[row-1][col-1];
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title="O(m*n)space"]</p>
<pre>
public class Solution {
    /**
     * @param grid: a list of lists of integers.
     * @return: An integer, minimizes the sum of all numbers along its path
     */
    public int minPathSum(int[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        
        int row = grid.length, col = grid[0].length;
        int[][] path = new int[row][col];
        for (int i = 0; i < row; i++) {
            if (i == 0) {
                path[i][0] = grid[i][0];
            } else {
                path[i][0] = grid[i][0] + path[i-1][0];
            }
        }
        for (int j = 1; j < col; j++) {
            path[0][j] += grid[0][j] + path[0][j-1];
        }
        
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                path[i][j] = Math.min(path[i-1][j], path[i][j-1]) + grid[i][j];
            }
        }
        return path[row-1][col-1];
    }
}
</pre>
<p>[/expand]</p>
