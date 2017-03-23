---
layout: post
title: Kth Smallest Number in Sorted Matrix
date: 2015-10-21 14:23:52.000000000 -04:00
tags:
- Algorithm
categories:
- Data Structure
- Matrix
author: Jason
---
<p><strong><em>Find the kth smallest number in at row and column sorted matrix.</em></strong></p>


``` java
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
```
