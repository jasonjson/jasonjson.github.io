---
layout: post
title: 270 - Closest Binary Search Tree Value
date: 2015-10-30 11:53:00.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.**


``` java
public class Solution {
    public int closestValue(TreeNode root, double target) {
        Stack<treenode> stack = new Stack<treenode>();
        int result = root.val;
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                if (Math.abs(root.val - target) < Math.abs(result - target)) {
                    result = root.val;
                }
                root = root.right;
            }
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """

        ret = root.val
        while root:
            if abs(ret - target) > abs(root.val - target):
                ret = root.val
            root = root.right if root.val <= target else root.left
        return ret
```
