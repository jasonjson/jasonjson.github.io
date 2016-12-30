---
layout: post
title: Dungeon Game
date: 2015-11-04 19:13:08.000000000 -05:00
type: post
published: true
status: publish
categories:
- Dynamic Programming
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468556649;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:151;}i:1;a:1:{s:2:"id";i:382;}i:2;a:1:{s:2:"id";i:533;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.<br />
The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.<br />
Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).<br />
In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.<br />
Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int row = dungeon.length, col = dungeon[0].length;
        int[][] health = new int[row][col];
        health[row - 1][col - 1] = Math.max(1 - dungeon[row - 1][col - 1], 1);
        for (int i = row - 2; i >= 0; i--) {
            health[i][col - 1] = Math.max(health[i + 1][col - 1] - dungeon[i][col - 1], 1);
        }
        for (int j = col - 2; j >= 0; j--) {
            health[row - 1][j] = Math.max(health[row - 1][j + 1] - dungeon[row - 1][j], 1);
        }
        for (int i = row - 2; i >= 0; i--) {
            for (int j = col - 2; j >= 0; j--) {
                health[i][j] = Math.max(Math.min(health[i + 1][j], health[i][j + 1]) - dungeon[i][j], 1);
                //找一条最小的路径 所以是Math.min(health[i + 1][j], health[i][j + 1])
            }
        }
        return health[0][0];
    }
}
</pre>
<p>[/expand]</p>
