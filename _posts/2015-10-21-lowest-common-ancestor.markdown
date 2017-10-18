---
layout: post
title: 236 - Lowest Common Ancestor
date: 2015-10-21 02:52:47.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes. The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.**


``` java
public class Solution {
    /**
     * @param root: The root of the binary search tree.
     * @param A and B: two nodes in a Binary.
     * @return: Return the least common ancestor(LCA) of the two nodes.
     */
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode A, TreeNode B) {
        if (root == null || root == A || root == B) return root;

        TreeNode left = lowestCommonAncestor(root.left, A, B);
        TreeNode right = lowestCommonAncestor(root.right, A, B);
        if (left != null && right != null) {
            return root;
        }
        return left == null ? right : left;
    }
}
```

``` python
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root or root == p or root == q:
            return root

        left_ancestor = self.lowestCommonAncestor(root.left, p, q)
        right_ancestor = self.lowestCommonAncestor(root.right, p, q)
        if left_ancestor and right_ancestor:
            return root
        else:
            return left_ancestor or right_ancestor
