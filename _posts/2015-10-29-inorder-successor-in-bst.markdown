---
layout: post
title: Inorder Successor in BST
date: 2015-10-29 13:37:23.000000000 -04:00
tags:
- Algorithm
categories:
- Data Structure
author: Jason
---
<p><strong><em>Given a binary search tree and a node in it, find the in-order successor of that node in the BST. Note: If the given node has no in-order successor in the tree, return null.</em></strong></p>


``` java
public class Solution {
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if (root == null || p == null) return null;
        
        Stack<treenode> stack = new Stack<treenode>();
        TreeNode prev = null;
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                if (prev == p) {
                    return root;
                }
                prev = root;
                root = root.right;
            }
        }
        return null;
    }
}
```
