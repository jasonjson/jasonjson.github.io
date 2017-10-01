---
layout: post
title: Binary Tree Upside Down
date: 2015-11-05 17:28:56.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
- Brain Teaser
author: Jason
---
<p><strong><em>Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.</em></strong></p>


``` java
public class Solution {
    public TreeNode upsideDownBinaryTree(TreeNode root) {
        if (root == null || (root.left == null && root.right == null)) return root;
        
        TreeNode newRoot = upsideDownBinaryTree(root.left);
        root.left.left = root.right;
        root.left.right = root;
        root.left = null;
        root.right = null;
        return newRoot;
    }
}
```
