---
layout: post
title: Rectangle Area
date: 2015-10-25 20:44:22.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
author: Jason
---
**Find the total area covered by two rectilinear rectangles in a 2D plane. Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.**

``` java
public class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        long result = 0;
        if (E >= C || A >= G || B >= H || F >= D) {
            result = (C - A) * (D - B) + (G - E) * (H - F);
        }//two rectangles are separate
        int x1 = Math.max(A, E);
        int y1 = Math.max(B, F);
        int x2 = Math.min(C, G);
        int y2 = Math.min(D, H);
        result = (C - A) * (D - B) + (G - E) * (H - F) - (x2 - x1) * (y2 - y1);//minus overlapped 
        if (result > Integer.MAX_VALUE) {
            return Integer.MAX_VALUE;
        } else {
            return result;
        }
    }
}
```
