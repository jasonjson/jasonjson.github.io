---
layout: post
title: Game of Life
date: 2015-10-28 15:02:31.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
- Matrix
author: Jason
---
<p><strong><em>Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):</em></strong></p>


<ul>
<li>Any live cell with fewer than two live neighbors dies, as if caused by under-population.</li>
<li>Any live cell with two or three live neighbors lives on to the next generation.</li>
<li>Any live cell with more than three live neighbors dies, as if by over-population..</li>
<li>Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.</li>
<li>Write a function to compute the next state (after one update) of the board given its current state.</li>
<li>0 : die to die</li>
<li>1 : live to live</li>
<li>2 : live to die</li>
<li>3 : die to live</li>
</ul>
<p><a href="http://www.cnblogs.com/grandyang/p/4854466.html">Read more</a></p>

``` java
public class Solution {
    public void gameOfLife(int[][] board) {
        if (board == null || board.length == 0) return;
        
        int row = board.length, col = board[0].length;
        int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                int count = 0;
                for (int k = 0; k < 8; k++) {
                    int newX = i + dx[k], newY = j + dy[k];
                    if (newX >= 0 && newX < row && newY >= 0 && newY < col && (board[newX][newY] == 1 || board[newX][newY] == 2)) {
                        count ++;
                    }
                }
                if (board[i][j] == 1 && (count < 2 || count > 3)) {
                    board[i][j] = 2;
                } else if (board[i][j] == 0 && count == 3) {
                    board[i][j] = 3;
                }
            }
        }
        
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                board[i][j] %= 2;
            }
        }
    }
}
```
