---
layout: post
title: 222 - Count Complete Tree Nodes
date: 2015-11-03 15:01:07.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a complete binary tree, count the number of nodes.**


``` java
public class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) return 0;

        int h = getDepth(root), count = 0;
        while (root != null) {
            if (getDepth(root.right) == h - 1) {
                count += 1 << (h - 1) - 1 + 1;//左边树是满的共有h-1层,左子树1 << (h - 1) - 1 加上 root: 1
                root = root.right;//计算可能不满的右子树
            } else {
                count += 1 << (h - 2) - 1 + 1;//右子树是满的共有h-2层，右子树1 << (h - 2) - 1 加上root: 1
                root = root.left;//计算不满的左子树
            }
            h--;
        }
        return count;
    }

    public int getDepth(TreeNode root) {
        int depth = 0;
        while (root != null) {
            depth++;
            root = root.left;
        }
        return depth;
    }
}
```

``` python
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = self.get_depth(root)
        count = 0
        while root:
            if self.get_depth(root.right) == depth - 1:
                count += 2 ** (depth - 1)
                root = root.right
            else:
                count += 2 ** (depth - 2)
                root = root.left
            depth -= 1
        return count

    def get_depth(self, root):
        depth = 0
        while root:
            depth += 1
            root = root.left
        return depth
