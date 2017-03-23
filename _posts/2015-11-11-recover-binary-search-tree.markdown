---
layout: post
title: Recover Binary Search Tree
date: 2015-11-11 17:51:55.000000000 -05:00
tags:
- Algorithm
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Two elements of a binary search tree (BST) are swapped by mistake.</p>

Recover the tree without changing its structure.</em></strong></p>
``` java
public class Solution {
    private TreeNode n1 = null, n2 = null, prev = null;
    public void recoverTree(TreeNode root) {
        if (root == null) return;
        recover(root);
        int temp = n1.val;
        n1.val = n2.val;
        n2.val = temp;
    }
    public void recover(TreeNode root) {
        if (root == null) return;
        recover(root.left);
        if (prev != null && prev.val > root.val) {
            if (n1 == null) {
                n1 = prev;
            }
            n2 = root;
        }
        prev = root;
        recover(root.right);
    }
}
```
``` java
public class Solution {
    public void recoverTree(TreeNode root) {
        if (null == root) return;
        
        Stack<treenode> stack = new Stack<treenode>();
        TreeNode node1 = null, node2 = null, prev = null;
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                if (prev != null && root.val < prev.val) {
                    if (node1 == null) {
                        node1 = prev;
                    } 
                    node2 = root;//we need to update both node1 and node2 here, otherwise for the case of two nodes only, node2 will be null
                }
                prev = root;
                root = root.right;
            }
        }
        int temp = node1.val;
        node1.val = node2.val;
        node2.val = temp;
    }
}
```
