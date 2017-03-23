---
layout: post
title: Segmemt Tree Build II
date: 2015-10-21 13:29:13.000000000 -04:00
tags:
- Algorithm
categories:
- Data Structure
author: Jason
---
<p><strong><em>Implement a build method with a given array, so that we can create a corresponding segment tree with every node value represent the corresponding interval max value in the array, return the root of this segment tree.</em></strong></p>


``` java
public class Solution {
    /**
     *@param A: a list of integer
     *@return: The root of Segment Tree
     */
    public SegmentTreeNode build(int[] A) {
        return build(0, A.length - 1, A);
    }
    
    public SegmentTreeNode build(int start, int end, int[]array) {//start and end are indexes of the array
        if(start > end) {
            return null;
        }
        SegmentTreeNode root = new SegmentTreeNode(start, end);
        if (start == end) {
            root.max = array[start];
        } else {
            int mid = (start + end) / 2;
            root.left = build(start, mid , array);
            root.right = build(mid + 1, end, array);
            root.max = Math.max(root.left.max, root.right.max);
        }
        return root;
    }
}
```
