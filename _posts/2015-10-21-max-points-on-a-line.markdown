---
layout: post
title: 149 - Max Points on a Line
date: 2015-10-21 14:29:12.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.**


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
        for (int i = 0; i < points.length; i++) {
            HashMap<Double, Integer> map = new HashMap<Double, Integer>();
            int samePoint = 0, sameX = 1;
            for (int j = 0; j < points.length; j++) {
               if (i != j) {
                   if (points[i].x == points[j].x && points[i].y == points[j].y) {
                       samePoint ++;
                   }
                   if (points[i].x == points[j].x) {
                       sameX ++;
                       continue;
                   }
                   double slope = (double)(points[i].y - points[j].y) / (double)(points[i].x - points[j].x);
                   if (map.containsKey(slope)) {
                       map.put(slope, map.get(slope) + 1);
                   } else {
                       map.put(slope, 2);
                   }
                   max = Math.max(max, map.get(slope) + samePoint);
               }
            }
            max = Math.max(max, sameX);
        }
        return max;
    }
}
```

``` python
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0

        ret = 0
        for i in xrange(len(points)):
            slope_map = {}
            same_point, same_x = 0, 1
            for j in xrange(len(points)):
                if i == j:
                    continue
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    same_point += 1
                if points[i].x == points[j].x:
                    same_x += 1
                    continue
                slope = float(points[j].y - points[i].y) / float(points[j].x - points[i].x)
                if slope in slope_map:
                    slope_map[slope] += 1
                else:
                    slope_map[slope] = 2
                ret = max(ret, same_point + slope_map[slope])
            ret = max(ret, same_x)
        return ret
```
