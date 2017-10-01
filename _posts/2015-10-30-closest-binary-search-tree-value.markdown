---
layout: post
title: Closest Binary Search Tree Value
date: 2015-10-30 11:53:00.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.</em></strong></p>


``` java
public class Solution {
    public int closestValue(TreeNode root, double target) {
        int result = root.val;
        while (root != null) {
            if (Math.abs(root.val - target) < Math.abs(result - target)) {
                result = root.val;
            }
            root = root.val > target ? root.left : root.right;
            //if root.val > target, then every node in right subtree will produce a bigger difference
        }
        return result;
    }
}
```
``` java
public class Solution {
    public int closestValue(TreeNode root, double target) {
        Stack<treenode> stack = new Stack<treenode>();
        int result = root.val;
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                if (Math.abs(root.val - target) < Math.abs(result - target)) {
                    result = root.val;
                }
                root = root.right;
            }
        }
        return result;
    }
}
```
