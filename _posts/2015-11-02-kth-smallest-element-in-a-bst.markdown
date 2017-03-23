---
layout: post
title: Kth Smallest Element in a BST
date: 2015-11-02 18:05:03.000000000 -05:00
tags:
- Algorithm
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.</em></strong></p>


``` java
public class Solution {
    public int kthSmallest(TreeNode root, int k) {
        if (root == null || k <= 0) return -1;
        Stack<treenode> stack = new Stack<treenode>();
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                if (k-- == 1) return root.val;
                root = root.right;
            }
        }
        return -1;
    }
}
```
