---
layout: post
title: Rotate Image
date: 2015-10-21 14:34:51.000000000 -04:00
type: post
published: true
status: publish
categories:
- Matrix
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1455035893;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:568;}i:1;a:1:{s:2:"id";i:165;}i:2;a:1:{s:2:"id";i:1495;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public void rotate(int[][] matrix) {
        if (matrix == null || matrix.length == 0) return;
        int n = matrix.length;
        for (int i = 0; i < n / 2; i++) {
            for (int j = i; j < n - i - 1; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - j - 1][i];//前一个row等于后一个col，前一个col + 后一个row = n - 1
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1];
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1];
                matrix[j][n - i - 1] = temp;
            }
        }
    }
}
</pre>
<p>[/expand]</p>
