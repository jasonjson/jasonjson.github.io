---
layout: post
title: Symmetric Tree
date: 2015-11-11 17:24:07.000000000 -05:00
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).</em></strong></p>

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
