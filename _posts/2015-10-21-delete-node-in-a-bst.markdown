---
layout: post
title: 450 - Delete Node in a BST
date: 2015-10-21 02:03:14.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.**


``` java
public class Solution {
    public TreeNode removeNode(TreeNode root, int value) {
        if (root == null) return null;

        if (root.val > value) {
            root.left = removeNode(root.left, value);
        } else if (root.val < value) {
            root.right = removeNode(root.right, value);
        } else {
            if (root.left == null) {
                return root.right;
            }
            int max = helper(root.left);
            root.val = max;
            root.left = removeNode(root.left, max);
        }
        return root;
    }

    public int helper(TreeNode root) {
        while (root.right != null) {
            root = root.right;
        }
        return root.val;
    }
}
```

``` python
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        if not root:
            return

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            else:
                max_val = self.find_max(root.left)
                root.val = max_val
                root.left = self.deleteNode(root.left, max_val)
        return root

    def find_max(self, root):
        while root.right:
            root = root.right
        return root.val
```
