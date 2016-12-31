---
layout: post
title: Count Complete Tree Nodes
date: 2015-11-03 15:01:07.000000000 -05:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469120444;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:264;}i:1;a:1:{s:2:"id";i:1058;}i:2;a:1:{s:2:"id";i:47;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a complete binary tree, count the number of nodes.</em></strong></p>
<p>[expand title = "iterative"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
<p>[expand title="recursive"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
