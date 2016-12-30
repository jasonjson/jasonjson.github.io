---
layout: post
title: Smallest Rectangle Enclosing Black Pixels
date: 2015-11-07 16:16:21.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469037099;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1903;}i:1;a:1:{s:2:"id";i:1148;}i:2;a:1:{s:2:"id";i:302;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.</em></strong></p>
<p>[expand title="O(n)"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
