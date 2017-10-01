---
layout: post
title: Smallest Rectangle Enclosing Black Pixels
date: 2015-11-07 16:16:21.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
<p><strong><em>An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.</em></strong></p>


``` java
public class Solution {
    int maxX = Integer.MIN_VALUE, minX = Integer.MAX_VALUE, maxY = Integer.MIN_VALUE, minY = Integer.MAX_VALUE;//find the largest and smallest x, y coordinates for black pixel
    public int minArea(char[][] image, int x, int y) {
        if (image == null || image.length == 0) return 0;
        dfs(image, x, y);
        return (maxX - minX + 1) * (maxY - minY + 1);
    }
    
    public void dfs(char[][] image, int x, int y) {
        int row = image.length, col = image[0].length;
        if (x < 0 || x >= row || y < 0 || y >= col || image[x][y] == '0') {
            return;
        }
        image[x][y] = '0';//can use boolean function to avoid modifying original matrix
        maxX = Math.max(maxX, x);
        minX = Math.min(minX, x);
        maxY = Math.max(maxY, y);
        minY = Math.min(minY, y);
        dfs(image, x - 1, y);
        dfs(image, x + 1, y);
        dfs(image, x, y - 1);
        dfs(image, x, y + 1);
    }
}
```
