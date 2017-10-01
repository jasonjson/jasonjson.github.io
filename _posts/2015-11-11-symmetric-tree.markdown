---
layout: post
title: Symmetric Tree
date: 2015-11-11 17:24:07.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).**


``` java
public class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return helper(root, root);
    }

    public boolean helper(TreeNode a, TreeNode b) {
        if (a == null && b == null) return true;
        if (a == null || b == null) return false;
        return a.val == b.val && helper(a.left, b.right) && helper(a.right, b.left);
    }
}
```

``` java
public class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        Queue<treenode> q1 = new LinkedList<treenode>();
        Queue<treenode> q2 = new LinkedList<treenode>();
        q1.offer(root);
        q2.offer(root);
        while (!q1.isEmpty() && !q2.isEmpty()) {
            TreeNode left = q1.poll();
            TreeNode right = q2.poll();
            if (left == null && right == null) continue;
            if (left == null || right == null || left.val != right.val) return false;
            q1.offer(left.left);
            q1.offer(left.right);
            q2.offer(right.right);
            q2.offer(right.left);
        }
        return q1.size() == q2.size();
    }
}
```

``` python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, root)

    def helper(self, left, right):
        if left is None and right is None:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.helper(left.left, right.right) and self.helper(left.right, right.left)
```
