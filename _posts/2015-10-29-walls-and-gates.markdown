---
layout: post
title: Walls and Gates
date: 2015-10-29 13:31:35.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465371275;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1903;}i:1;a:1:{s:2:"id";i:1148;}i:2;a:1:{s:2:"id";i:1506;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>You are given a m x n 2D grid initialized with these three possible values.<br />
-1 - A wall or an obstacle.<br />
0 - A gate.<br />
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.<br />
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public void wallsAndGates(int[][] rooms) {
        if (rooms == null || rooms.length == 0) return;
        for (int i = 0; i < rooms.length; i++) {
            for (int j = 0; j < rooms[0].length; j++) {
                if (rooms[i][j] == 0) {
                    helper(rooms, i, j);
                }
            }
        }
    }
    
    public void helper(int[][] rooms, int i, int j) {
        int[] dx = {-1, 0, 0, 1};
        int[] dy = {0, -1, 1, 0};
        for (int k = 0; k < 4; k++) {
            int x = i + dx[k], y = j + dy[k];
            if (x >= 0 && x < rooms.length && y >= 0 && y < rooms[0].length && rooms[x][y] > rooms[i][j] + 1) {
                //rooms[x][y] > rooms[i][j] + 1 确保只有INF才会被修改, 0 和 -1均不变
                rooms[x][y] = rooms[i][j] + 1;
                helper(rooms, x, y);
            }
        }
    }
}
</pre>
<p>[/expand]</p>
