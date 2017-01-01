---
layout: post
title: Inorder Successor in BST
date: 2015-10-29 13:37:23.000000000 -04:00
type: post
published: true
status: publish
categories:
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466101890;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1470;}i:1;a:1:{s:2:"id";i:290;}i:2;a:1:{s:2:"id";i:1058;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a binary search tree and a node in it, find the in-order successor of that node in the BST. Note: If the given node has no in-order successor in the tree, return null.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if (root == null || p == null) return null;
        
        Stack<treenode> stack = new Stack<treenode>();
        TreeNode prev = null;
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                if (prev == p) {
                    return root;
                }
                prev = root;
                root = root.right;
            }
        }
        return null;
    }
}
</treenode></treenode></pre>
<p>[/expand]</p>
