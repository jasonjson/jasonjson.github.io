---
layout: post
title: Lowest Common Ancestor of a Binary Search Tree
date: 2015-11-02 16:51:12.000000000 -05:00
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.</em></strong></p>

``` java
public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return null;
        if (root.val > p.val && root.val > q.val) {
            return lowestCommonAncestor(root.left, p, q);
        } else if (root.val < p.val && root.val < q.val) {
            return lowestCommonAncestor(root.right, p, q);
        } else {
            return root;
        }
    }
}
```
