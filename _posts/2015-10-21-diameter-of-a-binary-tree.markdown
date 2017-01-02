---
layout: post
title: Diameter of a Binary Tree
date: 2015-10-21 02:54:43.000000000 -04:00
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two leaves in the tree.</em></strong><br />


``` java
class Solution {
    /*
    * The diameter of a tree T is the largest of the following quantities:
    * the diameter of left subtree
    * the diameter of right subtree
    * the longest path between leaves that goes through the root of T
    * (this can be computed from the heights of the subtrees of T)
    */
    public int diameter(TreeNode root) {
        if (root == null) return 0;

        int leftHeight = getHeight(root.left);
        int rightHeight = getHeight(root.right);
        int leftDia = diameter(root.left);
        int rightDia = diameter(root.right);

        return Math.max(Math.max(leftDia, rightDia), leftHeight + 1 + rightHeight);
        //the maximum diameter might path the root, or on the left subtree, or in the right subtree
    }

    public int getHeight(TreeNode root) {
        if (root == null) return 0;
        return Math.max(getHeight(root.left), getHeight(root.right)) + 1;
    }
};
```
