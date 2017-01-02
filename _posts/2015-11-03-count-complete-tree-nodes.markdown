---
layout: post
title: Count Complete Tree Nodes
date: 2015-11-03 15:01:07.000000000 -05:00
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a complete binary tree, count the number of nodes.</em></strong></p>

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
``` java
public class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        int left = getDepth(root, 1);
        int right = getDepth(root, 2);
        if (left == right) {
            return (1 << left) - 1;//唯一的剪枝
        } else {
            return countNodes(root.left) + countNodes(root.right) + 1;//单独靠recursive会TLE
        }
    }
    
    public int getDepth(TreeNode node, int turn) {
        int dep = 0;
        while (node != null) {
            dep ++;
            if (turn == 1) node = node.left;
            if (turn == 2) node = node.right;
        }
        return dep;
    }
}
```
