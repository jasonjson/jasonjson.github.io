---
layout: post
title: Kth Smallest Element in a BST
date: 2015-11-02 18:05:03.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467981446;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:292;}i:1;a:1:{s:2:"id";i:1470;}i:2;a:1:{s:2:"id";i:1193;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int kthSmallest(TreeNode root, int k) {
        if (root == null || k <= 0) return -1;
        Stack<treenode> stack = new Stack<treenode>();
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                if (k-- == 1) return root.val;
                root = root.right;
            }
        }
        return -1;
    }
}
</treenode></treenode></pre>
<p>[/expand]</p>
