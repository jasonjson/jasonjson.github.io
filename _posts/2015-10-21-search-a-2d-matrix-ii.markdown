---
layout: post
title: Search a 2D Matrix II
date: 2015-10-21 02:31:22.000000000 -04:00
type: post
published: true
status: publish
categories:
- Matrix
- Sorting
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466112327;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:153;}i:1;a:1:{s:2:"id";i:549;}i:2;a:1:{s:2:"id";i:535;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it. This matrix has the following properties:<br />
Integers in each row are sorted from left to right.<br />
Integers in each column are sorted from up to bottom.<br />
No duplicate integers in each row or column.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @param: A number you want to search in the matrix
     * @return: An integer indicate the occurrence of target in the given matrix
     */
    public int searchMatrix(int[][] matrix, int target) {
        // write your code here
        int count = 0;
        if (matrix == null || matrix.length == 0) return count;
        if (matrix[0] == null || matrix[0].length == 0) return count;
        //error check
        int row = matrix.length, col = matrix[0].length;
        int i = 0, j = col - 1, count = 0;
        while (i < row && j >= 0) {
            if (matrix[i][j] == target) {
                count ++;
                j--;//bug: forget to decrement j, j is the smallest element in this column, the rest elements woule be larger
            } else if (matrix[i][j] > target) {
                j--;
            } else {
                i++;
            }
        }
        return count;
    }
}
</pre>
<p>[/expand]</p>
