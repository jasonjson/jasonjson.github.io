---
layout: post
title: Shortest Distance from All Buildings
date: 2015-12-16 22:42:54.000000000 -05:00
type: post
published: true
status: publish
categories:
- BFS
- Brain teaser
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468425991;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1148;}i:1;a:1:{s:2:"id";i:1159;}i:2;a:1:{s:2:"id";i:302;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You are given a 2D grid of values 0, 1 or 2, where:<br />
Each 0 marks an empty land which you can pass by freely.<br />
Each 1 marks a building which you cannot pass through.<br />
Each 2 marks an obstacle which you cannot pass through.<br />
The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
//this problem is only slightly different from "best meeting points", but the algorithm is quite different
public class Solution {
    public int shortestDistance(int[][] grid) {
        if (grid == null || grid.length == 0) return -1;
        
        int row = grid.length, col = grid[0].length;
        int[][] num = new int[row][col]; //visited buildings at each point
        int[][] dist = new int[row][col]; //total distance for each point
        int buildings = 0; //number of buidlings visited
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    buildings ++;
                    boolean[][] visited = new boolean[row][col];
                    Queue<int[]> q = new LinkedList<int[]>();
                    q.offer(new int[]{i, j});//[i][j] is like a root, we do bfs
                    int distance = 0;
                    while (!q.isEmpty()) {
                        int size = q.size();
                        for (int k = 0; k < size; k++) {
                            int[] point = q.poll();
                            int x = point[0], y = point[1];
                            num[x][y] ++;//one more point gets visited
                            dist[x][y] += distance;//update distance for this point
                            if (x - 1 >= 0 && grid[x - 1][y] == 0 && !visited[x - 1][y]) {
                                q.offer(new int[]{x - 1, y});
                                visited[x - 1][y] = true;
                            }
                            if (x + 1 < row && grid[x + 1][y] == 0 && !visited[x + 1][y]) {
                                q.offer(new int[]{x + 1, y});
                                visited[x + 1][y] = true;
                            }
                            if (y - 1 >= 0 && grid[x][y - 1] == 0 && !visited[x][y - 1]) {
                                q.offer(new int[]{x, y - 1});
                                visited[x][y - 1] = true;
                            }
                            if (y + 1 < col && grid[x][y + 1] == 0 && !visited[x][y + 1]) {
                                q.offer(new int[]{x, y + 1});
                                visited[x][y + 1] = true;
                            }
                        }
                        distance ++;
                    }
                }
            }
        }
        int result = Integer.MAX_VALUE;
        for (int i = 0; i < row; i ++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 0 && num[i][j] == buildings) {
                    result = Math.min(result, dist[i][j]);
                }
            }
        }
        return result == Integer.MAX_VALUE ? -1 : result;
    }
}
</pre>
<p>[/expand]</p>
