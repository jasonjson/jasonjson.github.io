---
layout: post
title: Building skyline Outline
date: 2015-10-21 14:47:55.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
- Data Structure
author: Jason
---
<p><strong><em>Given N buildings in a x-axis，each building is a rectangle and can be represented by a triple (start, end, height)，where start is the start position on x-axis, end is the end position on x-axis and height is the height of the building. Buildings may overlap if you see them from far away，find the outline of them. An outline can be represented by a triple, (start, end, height), where start is the start position on x-axis of the outline, end is the end position on x-axis and height is the height of the outline.</em></strong></p>


``` java
public class Solution {
    class Height {
        int index, height;
        Height (int index, int height) {
            this.index = index;
            this.height = height;
        }
    }
    public ArrayList<ArrayList<Integer>> buildingOutline(int[][] buildings) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (buildings == null || buildings.length == 0) return result;        
        ArrayList<height> heights = new ArrayList<height>();
        for (int[] building : buildings) {
            heights.add(new Height(building[0], -building[2]));
            heights.add(new Height(building[1], building[2]));
        }
        Collections.sort(heights, new Comparator<height>() {
            public int compare(Height h1, Height h2) {
                return h1.index != h2.index ? h1.index - h2.index : h1.height - h2.height; 
            }
        });
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>(10, Collections.reverseOrder());
        heap.add(0);
        int prev_height = 0, prev_index = 0;
        for (Height h : heights) {
            if (h.height < 0) {
                heap.add(-h.height);
            } else {
                heap.remove(h.height);
            }
            int curr = heap.peek();
            if (curr != prev_height) {
                if (prev_height != 0) {
                    ArrayList<Integer> list = new ArrayList<Integer>();
                    list.add(prev_index);
                    list.add(h.index);
                    list.add(prev_height);
                    result.add(list);
                }
                prev_index = h.index;
                prev_height = curr;
            }
        }
        return result;
    }
}//http://www.lintcode.com/en/problem/building-outline/#
```
