---
layout: post
title: Best Meeting Point
date: 2015-10-29 11:36:52.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Dynamic Programming
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468168324;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1903;}i:1;a:1:{s:2:"id";i:380;}i:2;a:1:{s:2:"id";i:589;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.</em></strong></p>
<p>[expand title="brutal force"]</p>
<pre>
public class Solution {
    public int minTotalDistance(int[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        int row = grid.length, col = grid[0].length;
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                min = Math.min(min, getDist(grid, i, j));
            }
        }
        return min;
    }
    
    public int getDist(int[][] grid, int x, int y) {
        int total = 0, row = grid.length, col = grid[0].length;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    total += Math.abs(i - x) + Math.abs(j - y);
                }
            }
        }
        return total;
    }
}
</pre>
<p>[/expand]<br />
[expand title = "O(mn)"]</p>
<pre>
public class Solution {
    public int minTotalDistance(int[][] grid) {
        return helper(grid, 0) + helper(grid, 1);
        //The point is that the distance can be separately measured for the horizontal and vertical directions, and the optimal point can also be chosen separately.
    }
    
    public int helper(int[][] grid, int dimen) {
        int row = grid.length, col = grid[0].length;
        List<integer> path = new ArrayList<integer>();
        if (dimen == 0) {
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < col; j++) {
                    if (grid[i][j] == 1) {
                        path.add(i);
                    }
                }
            }
        } else {
            for (int j = 0; j < col; j++) {
                for (int i = 0; i < row; i++) {
                    if (grid[i][j] == 1) {
                        path.add(j);
                    }
                }
            }
        }
        int total = 0, lo = 0, hi = path.size() - 1;
        while (lo < hi) {
            total += path.get(hi--) - path.get(lo++);
        }
        return total;
    }
}
</integer></integer></pre>
<p>[/expand]</p>
