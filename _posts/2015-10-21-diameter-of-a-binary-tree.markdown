---
layout: post
title: Diameter of a Binary Tree
date: 2015-10-21 02:54:43.000000000 -04:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463354011;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:2079;}i:1;a:1:{s:2:"id";i:1146;}i:2;a:1:{s:2:"id";i:260;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two leaves in the tree.</em></strong><br />
[expand title="code"]</p>
<pre>
class Solution {
    /*
    * The diameter of a tree T is the largest of the following quantities:
    * the diameter of left subtree
    * the diameter of right subtree
    * the longest path between leaves that goes through the root of T
    * (this can be computed from the heights of the subtrees of T)
    */
    public int diameter(TreeNode root) {
        if (root == null) return 0;

        int leftHeight = getHeight(root.left);
        int rightHeight = getHeight(root.right);
        int leftDia = diameter(root.left);
        int rightDia = diameter(root.right);

        return Math.max(Math.max(leftDia, rightDia), leftHeight + 1 + rightHeight);
        //the maximum diameter might path the root, or on the left subtree, or in the right subtree
    }

    public int getHeight(TreeNode root) {
        if (root == null) return 0;
        return Math.max(getHeight(root.left), getHeight(root.right)) + 1;
    }
};
</pre>
<p>[/expand]</p>
