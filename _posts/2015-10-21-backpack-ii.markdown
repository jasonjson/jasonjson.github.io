---
layout: post
title: Backpack II
date: 2015-10-21 03:57:56.000000000 -04:00
type: post
published: true
status: publish
categories:
- Dynamic Programming
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464666380;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:349;}i:1;a:1:{s:2:"id";i:45;}i:2;a:1:{s:2:"id";i:499;}}}}
  _inbound_impressions_count: '0'
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given n items with size Ai and value Vi, and a backpack with size m. What's the maximum value can you put into the backpack?</em></strong><br />
[expand title="O(m*n)space"]</p>
<pre>
public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A & V: Given n items with size A[i] and value V[i]
     * @return: The maximum value
     */
    public int backPackII(int m, int[] A, int V[]) {
        // write your code here
        int[][] value = new int[A.length + 1][m + 1];
        
        for (int i = 1; i <= A.length; i++) {
            for (int j = 1; j <= m; j++) {
                if (j >= A[i - 1]) {
                    value[i][j] = Math.max(value[i-1][j-A[i-1]] + V[i-1], value[i-1][j]);
                } else {
                    value[i][j] = value[i-1][j];
                }
            }
        }
        return value[A.length][m];
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title = "O(m)space"]</p>
<pre>
public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A & V: Given n items with size A[i] and value V[i]
     * @return: The maximum value
     */
    public int backPackII(int m, int[] A, int V[]) {
        int n = A.length;
        int[] total = new int[m+1];//we overwrite total each iteration
        for (int i = 0; i < n; i++) {
            for (int j = m; j >= 0; j--) {//j starts from m
                if (j == 0) {
                    total[j] = 0;
                } else if (j - A[i] >= 0) {
                    total[j] = Math.max(total[j - A[i]] + V[i], total[j]);
                }
            }
        }
        return total[m];
    }
}
</pre>
<p>[/expand]</p>
