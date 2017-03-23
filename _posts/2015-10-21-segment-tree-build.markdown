---
layout: post
title: Segment Tree Build
date: 2015-10-21 13:28:38.000000000 -04:00
tags:
- Algorithm
categories:
- Data Structure
author: Jason
---
<p><strong><em>The structure of Segment Tree is a binary tree which each node has two attributes start and end denote an segment / interval. start and end are both integers, they should be assigned in following rules:</em></strong></p>


<ol>
<li>The root's start and end is given by build method.</li>
<li>The left child of node A has start=A.left, end=(A.left + A.right)</li>
<li>The right child of node A has start=(A.left + A.right) / 2 + 1, end=A.right.</li>
<li>If start equals to end, there will be no children for this node</li>
</ol>
<p><strong><em>Implement a build method with two parameters start and end, so that we can create a corresponding segment tree with every node has the correct start and end value, return the root of this segment tree.</em></strong></p>


``` java
/**
 * Definition of SegmentTreeNode:
 * public class SegmentTreeNode {
 *     public int start, end;
 *     public SegmentTreeNode left, right;
 *     public SegmentTreeNode(int start, int end) {
 *         this.start = start, this.end = end;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     *@param start, end: Denote an segment / interval
     *@return: The root of Segment Tree
     */
    public SegmentTreeNode build(int start, int end) {
        if (start > end) return null;
        SegmentTreeNode root = new SegmentTreeNode(start, end);
        //if (start == end) return; we need to handle this corner case
        if (start < end) {
            int mid = (start + end) / 2;
            root.left = build(start, mid);
            root.right = build(mid + 1, end);
        }
        return root;
    }
}
```
