---
layout: post
title: Set Matrix Zeroes
date: 2015-10-21 14:36:15.000000000 -04:00
type: post
published: true
status: publish
categories:
- Matrix
tags: []
meta:
  _wpcom_is_markdown: '1'
  _wpas_done_all: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463801139;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1495;}i:1;a:1:{s:2:"id";i:1613;}i:2;a:1:{s:2:"id";i:564;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public void setZeroes(int[][] matrix) {
        if (matrix == null || matrix.length == 0) return;        
        int row = matrix.length, col = matrix[0].length;
        boolean[] rowZero = new boolean[row];
        boolean[] colZero = new boolean[col];
        for (int i = 0; i < row; i ++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 0) {
                    rowZero[i] = true;
                    colZero[j] = true;
                }
            }
        }        
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (rowZero[i] || colZero[j]) {
                    matrix[i][j] = 0;
                } 
            }
        }
    }O(m + n) space
    public void setZeroes(int[][] matrix) {
        if (matrix == null || matrix.length == 0) return;
        int row = matrix.length, col = matrix[0].length;
        boolean firstRowZero = false, firstColZero = false;
        for (int i = 0; i < row; i++) {
            if (matrix[i][0] == 0) {
                firstColZero = true;
                break;
            }//if first col has zero
        }
        for (int j = 0; j < col; j++) {
            if (matrix[0][j] == 0) {
                firstRowZero = true;
                break;
            }//if first row has zero
        }
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                if (matrix[i][j] == 0) {
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }//use first col and first row to store info
        }
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                if (matrix[0][j] == 0 || matrix[i][0] == 0){
                    matrix[i][j] = 0;
                }
            }//set elements to zero
        }
        if (firstRowZero) {
            for (int j = 0; j < col; j++) {
                matrix[0][j] = 0;
            }//set first row
        }
        if (firstColZero) {
            for (int i = 0; i < row; i++) {
                matrix[i][0] = 0;
            }//set first col
        }
    }
}//constant space
</pre>
<p>[/expand]</p>
