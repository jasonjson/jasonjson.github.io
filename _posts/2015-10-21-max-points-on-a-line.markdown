---
layout: post
title: Max Points on a Line
date: 2015-10-21 14:29:12.000000000 -04:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.</em></strong></p>

``` java
public class Solution {
    /**
     * @param points an array of point
     * @return an integer
     */
    public int maxPoints(Point[] points) {
        // Write your code here
        if (points == null || points.length == 0) return 0;

        int max = 0;
        //use point[i] as starting point, find all points with the same slope, or with same x and y, or with same x (in vertical line).
        for (int i = 0; i < points.length; i++) {
            HashMap<Double, Integer> map = new HashMap<Double, Integer>();
            int samePoint = 0, sameX = 1;//bug sameX starts from 1
            for (int j = 0; j < points.length; j++) {
               if (i != j) {//can't compare with itself
                   if (points[i].x == points[j].x && points[i].y == points[j].y) {
                       samePoint ++;
                   }
                   if (points[i].x == points[j].x) {
                       sameX ++;//this will also execude for samePoint
                       continue;//deal with vertical line, slope is infinity
                   }
                   double slope = (double)(points[i].y - points[j].y) / (double)(points[i].x - points[j].x);
                   if (map.containsKey(slope)) {
                       map.put(slope, map.get(slope) + 1);
                   } else {
                       map.put(slope, 2);//!!注意此处是2，不是1
                   }
                   max = Math.max(max, map.get(slope) + samePoint);
                   //the points with same slopes and the samePoint
               } 
            }
            max = Math.max(max, sameX);
            //check the number of points in vertical line
        }
        return max;
    }
}
```
