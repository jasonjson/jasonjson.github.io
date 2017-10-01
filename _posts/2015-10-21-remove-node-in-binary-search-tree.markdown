---
layout: post
title: Remove Node in Binary Search Tree
date: 2015-10-21 02:03:14.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a root of Binary Search Tree with unique value for each node.  Remove the node with given value. If there is no such a node with given value in the binary search tree, do nothing. You should keep the tree still a binary search tree after removal.</em></strong></p>


``` java
public class Solution {
    public TreeNode removeNode(TreeNode root, int value) {
        if (root == null) return null;
        
        if (root.val > value) {
            root.left = removeNode(root.left, value);
        } else if (root.val < value) {
            root.right = removeNode(root.right, value);
        } else {
            if (root.left == null) {
                return root.right;
            }
            int max = helper(root.left);
            root.val = max;
            root.left = removeNode(root.left, max);
        }
        return root;
    }
    
    public int helper(TreeNode root) {
        while (root.right != null) {
            root = root.right;
        }
        return root.val;
    }
}
```
