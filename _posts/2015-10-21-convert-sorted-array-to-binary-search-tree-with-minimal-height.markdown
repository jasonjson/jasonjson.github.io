---
layout: post
title: Convert Sorted Array to Binary Search Tree With Minimal Height
date: 2015-10-21 02:59:05.000000000 -04:00
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a sorted (increasing order) array, Convert it to create a binary tree with minimal height.</em></strong><br />


``` java
public class Solution {
    /**
     * @param A: an integer array
     * @return: a tree node
     */
    public TreeNode sortedArrayToBST(int[] A) {  
        if (A == null || A.length == 0) return null;
        return sortedArrayToBSTUtil(A, 0, A.length - 1);
    }
    
    public TreeNode sortedArrayToBSTUtil(int[] A, int start, int end) {
        if (start > end) return null;
        int mid = start + (end - start) / 2;
        TreeNode root = new TreeNode(A[mid]);
        root.left = sortedArrayToBSTUtil(A, start, mid - 1);
        root.right = sortedArrayToBSTUtil(A, mid + 1, end);
        return root;
    }
}
```
