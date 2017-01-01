---
layout: post
title: Spiral Matrix
date: 2015-11-14 19:20:05.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Matrix
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464401919;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:165;}i:1;a:1:{s:2:"id";i:1069;}i:2;a:1:{s:2:"id";i:2052;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public List<integer> spiralOrder(int[][] matrix) {
        List<integer> result = new ArrayList<integer>();
        if (matrix == null || matrix.length == 0) return result;
        
        int up = 0, down = matrix.length - 1, left = 0, right = matrix[0].length - 1;
        while (true) {
            for (int j = left; j <= right; j++) {
                result.add(matrix[up][j]);//print top row
            }
            up ++;
            if (crossBoundary(up, down, left, right)) {
                break;
            }            
            for (int i = up; i <= down; i++) {
                result.add(matrix[i][right]);//print right col
            }
            right--;
            if (crossBoundary(up, down, left, right)) {
                break;
            }            
            for (int j = right; j >= left; j--) {
                result.add(matrix[down][j]);//print bottom row
            }
            down --;
            if (crossBoundary(up, down, left, right)) {
                break;
            }            
            for (int i = down; i >= up; i--) {
                result.add(matrix[i][left]);//print left col
            }
            left ++;
            if (crossBoundary(up, down, left, right)) {
                break;
            }
        }
        return result;
    }    
    public boolean crossBoundary(int up, int down, int left, int right) {
        return up > down || left > right;
    }
}
</integer></integer></integer></pre>
<p>[/expand]</p>
