---
layout: post
title: 101 - Symmetric Tree
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

        return self.helper(root, root)

    def helper(self, left, right):
        if not left or not right:
            return left == right
        return left.val == right.val and self.helper(left.left, right.right) and self.helper(left.right, right.left)
```

``` python
class Solution:
    def isSymmetric(self, root):

        q1, q2 = [root], [root]
        while q1 and q2:
            left = q1.pop()
            right = q2.pop()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            q1.append(left.left)
            q1.append(left.right)
            q2.append(right.right)
            q2.append(right.left)
        return not q1 and not q2
```
