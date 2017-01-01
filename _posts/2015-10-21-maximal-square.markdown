---
layout: post
title: Maximal Square
date: 2015-10-21 14:29:56.000000000 -04:00
type: post
published: true
status: publish
categories:
- Dynamic Programming
- Matrix
tags: []
meta:
  _wpas_done_all: '1'
  _spost_short_title: ''
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466310233;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1296;}i:1;a:1:{s:2:"id";i:1482;}i:2;a:1:{s:2:"id";i:1852;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param matrix: a matrix of 0 and 1
     * @return: an integer
     */
    public int maxSquare(int[][] matrix) {
        // write your code here
        if (matrix == null || matrix.length == 0) return 0;
        int row = matrix.length, col = matrix[0].length;
        
        int[][] dp = new int[row][col];
        int max = 0;
        for (int i = 0; i < row; i++) {
            if (matrix[i][0] == 1) {
                dp[i][0] = 1;
                max = 1;
            }
        }
        
        for (int j = 0; j < col; j++) {
            if (matrix[0][j] == 1) {
                dp[0][j] = 1;
                max = 1;
            }
        }
        
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                if (matrix[i][j] == 1) {
                    dp[i][j] = Math.min(dp[i-1][j], Math.min(dp[i][j-1], dp[i-1][j-1])) + 1;
                    max = Math.max(max, dp[i][j]);
                }
            }
        }
        return max * max;
    }
}//http://www.cnblogs.com/jcliBlogger/p/4548751.html
</pre>
<p>[/expand]</p>
