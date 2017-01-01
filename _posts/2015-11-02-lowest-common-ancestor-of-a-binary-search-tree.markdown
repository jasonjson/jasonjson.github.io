---
layout: post
title: Lowest Common Ancestor of a Binary Search Tree
date: 2015-11-02 16:51:12.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1462920823;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1198;}i:1;a:1:{s:2:"id";i:1277;}i:2;a:1:{s:2:"id";i:286;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return null;
        if (root.val > p.val && root.val > q.val) {
            return lowestCommonAncestor(root.left, p, q);
        } else if (root.val < p.val && root.val < q.val) {
            return lowestCommonAncestor(root.right, p, q);
        } else {
            return root;
        }
    }
}
</pre>
<p>[/expand]</p>
