---
layout: post
title: Insert Node in a Binary Search Tree
date: 2015-10-21 02:08:49.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.</em></strong></p>


``` java
public class Solution {
    /*** @param root: The root of the binary search tree.
     * @param node: insert this node into the binary search tree*/
    public TreeNode insertNode(TreeNode root, TreeNode node) {
        if (root == null) return node;//base case!!!
        if (node == null) return root;
        if (node.val <= root.val){
            if (root.left != null) { 
                root.left = insertNode(root.left, node);
            } else { 
                root.left = node;
            }
        } else {
            if (root.right != null) {
                root.right = insertNode(root.right, node);
            } else { 
                root.right = node;
            }
        }
        return root;
    }   
    //iterative approach
    public TreeNode insertNode(TreeNode root, TreeNode node) {    
        if (root == null) return node;
        if (node == null) return root;
        TreeNode curr = root;
        while (curr != null) {
            if (node.val <= curr.val && curr.left == null) {
                curr.left = node;
                break; //first check null, then move
            } else if (node.val > curr.val && curr.right == null) {
                curr.right = node;
                break;// don't forget to break!!!
            } else if (node.val <= curr.val) { 
                curr = curr.left;
            } else { 
                curr = curr.right;
            }
        }
        return root;
    }
}
```
