---
layout: post
title: Unique Paths II
date: 2015-10-21 12:25:56.000000000 -04:00
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
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466794612;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:382;}i:1;a:1:{s:2:"id";i:380;}i:2;a:1:{s:2:"id";i:302;}}}}
  _inbound_impressions_count: '0'
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Follow up for "Unique Paths": Now consider if some obstacles are added to the grids. How many unique paths would there be? An obstacle and empty space is marked as 1 and 0 respectively in the grid.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param obstacleGrid: A list of lists of integers
     * @return: An integer
     */
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        // write your code here
        int m = obstacleGrid.length, n = obstacleGrid[0].length;
        
        int[][] paths = new int[m][n];
        //int[0][0] = 0 bug: the first element can be 1
        for (int i = 0; i < m; i++) {
            if (obstacleGrid[i][0] == 1) {
                break; //// for the first column, if [j][0] == 0, then there is no paths to any elements after this one, we can break, use default value 0
            } else {
                paths[i][0] = 1;
            }
        }
        
        for (int j = 0; j < n; j ++) {
            if (obstacleGrid[0][j] == 1) {
                break; // for the first row, if [0][j] == 0, then there is no paths to any elements after this one, we can break, use default value 0 
            } else {
                paths[0][j] = 1;
            }
        }// not able to put the above two together
        
        for (int i = 1; i < m; i ++) {
            for (int j = 1; j < n; j++) {
                if (obstacleGrid[i][j] == 1) {
                    continue;//not break!! we need to continue increment j
                } else {
                    paths[i][j] = paths[i-1][j] + paths[i][j-1];
                }
            }
        }
        return paths[m-1][n-1];
    }
}
</pre>
<p>[/expand]</p>
