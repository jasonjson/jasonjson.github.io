---
layout: post
title: The Skyline Problem
date: 2015-10-21 14:47:31.000000000 -04:00
categories:
- Brain teaser
- Data Structure
author: Jason
---
<p><strong><em>A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).</em></strong></p>

``` java
public class Solution {
    class Height {
        int index, height;
        Height (int index, int height) {
            this.index = index;
            this.height = height;
        }
    }
    public List<int[]> getSkyline(int[][] buildings) {
        List<int[]> result = new ArrayList<int[]>();
        if (buildings == null || buildings.length == 0) return result;        
        ArrayList<height> heights = new ArrayList<height>();
        for (int[] building : buildings) {
            heights.add(new Height(building[0], - building[2]));
            heights.add(new Height(building[1], building[2]));
        }
        Collections.sort(heights, new Comparator<height>() {
            public int compare(Height a, Height b) {
                return a.index == b.index ? a.height - b.height : a.index - b.index;
            }
        });
        PriorityQueue<integer> heap = new PriorityQueue<integer>(10, Collections.reverseOrder());
        heap.offer(0);
        int prev = 0;
        for (Height h : heights) {
            if (h.height < 0) {
                heap.offer(-h.height);
            } else {
                heap.remove(h.height);
            }
            int curr = heap.peek();
            if (curr != prev) {//merge same height points
                result.add(new int[] {h.index, curr});
                prev = curr;
            }
        }
        return result;
    }
}//http://codechen.blogspot.com/2015/06/leetcode-skyline-problem.html
```
