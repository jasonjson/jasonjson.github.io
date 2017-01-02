---
layout: post
title: Balanced Binary Tree
date: 2015-10-21 02:51:52.000000000 -04:00
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary tree, determine if it is height-balanced. For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.</em></strong><br />


``` java
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: True if this Binary tree is Balanced, or false.
     */
    public boolean isBalanced(TreeNode root){
        return getHeight(root) != -1; 
        
    }
    
    public int getHeight(TreeNode root){
        if (root == null) return 0;
        
        int left = getHeight(root.left);
        int right = getHeight(root.right);
        if (left == -1 || right == -1 || Math.abs(left - right) > 1) {
            return -1;
        }
        return Math.max(left, right) + 1;
    }
}
```
