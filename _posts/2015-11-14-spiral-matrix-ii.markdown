---
layout: post
title: Spiral Matrix II
date: 2015-11-14 19:28:04.000000000 -05:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
- Matrix
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466844873;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1495;}i:1;a:1:{s:2:"id";i:165;}i:2;a:1:{s:2:"id";i:585;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int[][] generateMatrix(int n) {
       int number = 1;
       int up = 0, down = n - 1, left = 0, right = n - 1;
       int[][] matrix = new int[n][n];
       while (number <= n * n) {
           for (int j = left; j <= right; j++) {
               matrix[up][j] = number ++;
           }
           up ++;
           for (int i = up; i <= down; i++) {
               matrix[i][right] = number ++;
           }
           right--;
           for (int j = right; j >= left; j--) {
               matrix[down][j] = number ++;
           }
           down --;
           for (int i = down; i >= up; i--) {
               matrix[i][left] = number ++;
           }
           left ++;
       }//while loop stops when we use up all numbers
       return matrix;
    }
}
</pre>
<p>[/expand]</p>
