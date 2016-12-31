---
layout: post
title: Search a 2D Matrix
date: 2015-10-21 02:28:30.000000000 -04:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
- Matrix
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466105168;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:165;}i:1;a:1:{s:2:"id";i:549;}i:2;a:1:{s:2:"id";i:535;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties: Integers in each row are sorted from left to right. The first integer of each row is greater than the last integer of the previous row.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param matrix, a list of lists of integers
     * @param target, an integer
     * @return a boolean, indicate whether matrix contains target
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        // write your code here
        if (matrix == null || matrix.length == 0) return false;
        if (matrix[0] == null || matrix[0].length == 0) return false;
        int row = matrix.length, col = matrix[0].length;
        int lo = 0, hi = row * col - 1;
        while (lo <= hi){
            int mid = (lo + hi) / 2;
            int number = matrix[mid/col][mid%col];
            if (number == target) {
                return true;
            }else if (number > target) {
                hi = mid - 1;
            }else {
                lo = mid + 1;
            }
        }
        return false;
    }
}
</pre>
<p>[/expand]</p>
