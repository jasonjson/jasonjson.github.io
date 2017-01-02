---
layout: post
title: Populating Next Right Pointers in Each Node
date: 2015-11-09 17:36:58.000000000 -05:00
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary tree, populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL. Initially, all next pointers are set to NULL.</em></strong></p>


``` java
public class Solution {
    public void connect(TreeLinkNode root) {
        if (root == null || (root.left == null && root.right == null)) return;
        root.left.next = root.right;
        if (root.next != null) root.right.next = root.next.left;
        connect(root.left);
        connect(root.right);
    }
}
```

``` java
public class Solution {
    public void connect(TreeLinkNode root) {
        if (root == null) return;
        
        Queue<treelinknode> q = new LinkedList<treelinknode>();
        q.offer(root);
        while (!q.isEmpty()) {
            int size = q.size();
            TreeLinkNode prev = null;
            for (int i = 0; i < size; i++) {
                TreeLinkNode curr = q.poll();
                if (prev != null) {
                    prev.next = curr;
                }
                prev = curr;
                if (curr.left != null) q.offer(curr.left);
                if (curr.right != null) q.offer(curr.right);
            }
        }
    }
}
```
