---
layout: post
title: Balanced Binary Tree
date: 2015-10-21 02:51:52.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1457109215;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:47;}i:1;a:1:{s:2:"id";i:270;}i:2;a:1:{s:2:"id";i:290;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a binary tree, determine if it is height-balanced. For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: True if this Binary tree is Balanced, or false.
     */
    public boolean isBalanced(TreeNode root){
        return getHeight(root) != -1; 
        
    }
    
    public int getHeight(TreeNode root){
        if (root == null) return 0;
        
        int left = getHeight(root.left);
        int right = getHeight(root.right);
        if (left == -1 || right == -1 || Math.abs(left - right) > 1) {
            return -1;
        }
        return Math.max(left, right) + 1;
    }
}
</pre>
<p>[/expand]</p>
