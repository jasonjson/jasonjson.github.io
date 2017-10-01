---
layout: post
title: 117 - Populating Next Right Pointers in Each Node II
date: 2015-11-09 18:52:59.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Follow up for problem "Populating Next Right Pointers in Each Node". What if the given tree could be any binary tree? Would your previous solution still work?**


``` java
public class Solution {
    public void connect(TreeLinkNode root) {
        if (root == null) return;

        TreeLinkNode curr = root;
        while (curr != null) {
            if (curr.left != null) {
                curr.left.next = curr.right != null ? curr.right : getNext(curr.next);
            }
            if (curr.right != null) {
                curr.right.next = getNext(curr.next);
            }
            curr = curr.next;
        }
        connect(root.left);
        connect(root.right);
    }

    public TreeLinkNode getNext(TreeLinkNode root) {
        while (root != null) {
            if (root.left != null) return root.left;
            if (root.right != null) return root.right;
            root = root.next;
        }
        return null;
    }
}
```

``` python
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, node):
        curr = dummy = TreeLinkNode(0)
        while node:
            curr.next = node.left
            if curr.next:
                curr = curr.next
            curr.next = node.right
            if curr.next:
                curr = curr.next
            node = node.next
            if not node:
                curr = dummy #dummy储存了连好的本层所有nodes
                node = dummy.next
```
