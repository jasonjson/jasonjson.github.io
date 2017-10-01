---
layout: post
title: Lowest Common Ancestor
date: 2015-10-21 02:52:47.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes. The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.</em></strong></p>


``` java
public class Solution {
    /**
     * @param root: The root of the binary search tree.
     * @param A and B: two nodes in a Binary.
     * @return: Return the least common ancestor(LCA) of the two nodes.
     */
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode A, TreeNode B) {
        if (root == null || root == A || root == B) return root;
        //once root == A or root == B, we just ouput the root, goes all way up
        
        TreeNode left = lowestCommonAncestor(root.left, A, B);
        //for instance, if root == A in left subtree, this root will goes all way up to be left;
        TreeNode right = lowestCommonAncestor(root.right, A, B);
        
        if (left != null && right != null) {
            //A and B are in different subtree
            return root;
        }
        return left == null ? right : left;
        //A are B are in the same side, either A is first found or B is first found
    }
}
```
