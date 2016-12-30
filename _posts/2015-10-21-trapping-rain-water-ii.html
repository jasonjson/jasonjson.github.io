---
layout: post
title: Trapping Rain Water II
date: 2015-10-21 14:41:51.000000000 -04:00
type: post
published: true
status: publish
categories:
- Dynamic Programming
- Matrix
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469175498;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:535;}i:1;a:1:{s:2:"id";i:1903;}i:2;a:1:{s:2:"id";i:1949;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given n x m non-negative integers representing an elevation map 2d where the area of each cell is 1 x 1, compute how much water it is able to trap after raining.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public class cell {
        int x, y, h;
        public cell (int x, int y, int h) {
            this.x = x;
            this.y = y;
            this.h = h;
        }
    }
    public int trapRainWater(int[][] heights) {
        if (heights == null || heights.length == 0) return 0;
        int row = heights.length, col = heights[0].length, result = 0;
        
        PriorityQueue<cell> heap = new PriorityQueue<cell>(10, new Comparator<cell>() {
            public int compare(cell a, cell b) {
                return a.h - b.h;
            }
        });        
        boolean[][] visited = new boolean[row][col];
        for (int i = 0; i < row; i++) {
            heap.add(new cell(i, 0, heights[i][0]));
            heap.add(new cell(i, col - 1, heights[i][col-1]));
            visited[i][0] = true;//mark true when add to heap
            visited[i][col - 1] = true;
        }
        for (int j = 0; j < col; j++) {
            heap.add(new cell(0, j, heights[0][j]));
            heap.add(new cell(row - 1, j, heights[row - 1][j]));
            visited[0][j] = true;
            visited[row - 1][j] = true;
        }
        while (!heap.isEmpty()) {
            cell c = heap.poll();
            result += calWater(heap, heights, visited, c.x + 1, c.y, c.h); 
            result += calWater(heap, heights, visited, c.x - 1, c.y, c.h);
            result += calWater(heap, heights, visited, c.x, c.y - 1, c.h);
            result += calWater(heap, heights, visited, c.x, c.y + 1, c.h);
        }
        return result;
    }    
    public int calWater(PriorityQueue<cell> heap, int[][] heights, boolean[][] visited, int x, int y, int h) {
        int row = heights.length, col = heights[0].length;
        if (x < 0 || x >= row || y < 0 || y >= col || visited[x][y]) return 0;
        heap.add(new cell(x, y, Math.max(h, heights[x][y])));
        visited[x][y] = true;
        return Math.max(0, h - heights[x][y]);//can hold water
    }
};//http://www.meetqun.com/thread-9868-1-1.html
</cell></cell></cell></cell></pre>
<p>[/expand]</p>
