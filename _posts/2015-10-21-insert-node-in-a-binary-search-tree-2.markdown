---
layout: post
title: Insert Node in a Binary Search Tree
date: 2015-10-21 02:57:36.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.</em></strong></p>


``` java
public class Solution {
    /**
     * @param root: The root of the binary search tree.
     * @param node: insert this node into the binary search tree
     * @return: The root of the new binary search tree.
     */
    public TreeNode insertNode(TreeNode root, TreeNode node) {
        if (root == null) return node;
        if (node == null) return root;
        
        if (node.val < root.val) {
            root.left = insertNode(root.left, node);
        } else {
            root.right = insertNode(root.right, node);
        }
        return root;
    }
    
    public TreeNode insertNode(TreeNode root, TreeNode node) {
        if (root == null) return node;
        if (node == null) return root;
        
        TreeNode curr = root;
        while (curr != null) {
            if (node.val <= curr.val) {
                if (curr.left == null) {
                    curr.left = node;
                    return root;//must return root here, otherwise dead while loop
                } else {
                    curr = curr.left;
                }
            } else {
                if (curr.right == null) {
                    curr.right = node;
                    return root;
                } else {
                    curr = curr.right;
                }
            }
        }
        return root;
    }
}
```
