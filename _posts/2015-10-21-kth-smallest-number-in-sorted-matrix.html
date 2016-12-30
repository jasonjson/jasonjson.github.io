---
layout: post
title: Kth Smallest Number in Sorted Matrix
date: 2015-10-21 14:23:52.000000000 -04:00
type: post
published: true
status: publish
categories:
- Data Structure
- Matrix
tags: []
meta:
  _edit_last: '1'
  _wpas_done_all: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469269325;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:302;}i:1;a:1:{s:2:"id";i:1824;}i:2;a:1:{s:2:"id";i:165;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Find the kth smallest number in at row and column sorted matrix.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param matrix: a matrix of integers
     * @param k: an integer
     * @return: the kth smallest number in the matrix
     */
    class point {
        int x, y, val;
        point(int x, int y, int val) {
            this.x = x;
            this.y = y;
            this.val = val;
        }
    }
    public int kthSmallest(int[][] matrix, int k) {
        // write your code here
        if (matrix == null || matrix.length == 0) return 0;
        
        int result = 0;
        PriorityQueue<point> pq = new PriorityQueue<point>(k, new Comparator<point>() {
           public int compare(point a, point b) {
               return a.val - b.val;
           } 
        });
        
        boolean[][] visited = new boolean[matrix.length][matrix[0].length];
        pq.offer(new point(0, 0, matrix[0][0]));
        visited[0][0] = true;
        for (int i = 0; i < k; i++) {
            point curr = pq.poll();
            result = curr.val;
            set(curr.x + 1, curr.y, matrix, pq, visited);
            set(curr.x, curr.y + 1, matrix, pq, visited);
        }
        return result;
    }
    
    public void set(int x, int y, int[][] matrix, PriorityQueue<point> pq, boolean[][] visited) {
        if (x >= matrix.length || y >= matrix[0].length || visited[x][y]) return;
        pq.offer(new point(x, y, matrix[x][y]));
        visited[x][y] = true;
    }
}
</point></point></point></point></pre>
<p>[/expand]</p>
