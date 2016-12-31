---
layout: post
title: Closest Binary Search Tree Value
date: 2015-10-30 11:53:00.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469292117;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1193;}i:1;a:1:{s:2:"id";i:61;}i:2;a:1:{s:2:"id";i:252;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.</em></strong></p>
<p>[expand title="O(lgn)"]</p>
<pre>
public class Solution {
    public int closestValue(TreeNode root, double target) {
        int result = root.val;
        while (root != null) {
            if (Math.abs(root.val - target) < Math.abs(result - target)) {
                result = root.val;
            }
            root = root.val > target ? root.left : root.right;
            //if root.val > target, then every node in right subtree will produce a bigger difference
        }
        return result;
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title="O(n)"]</p>
<pre>
public class Solution {
    public int closestValue(TreeNode root, double target) {
        Stack<treenode> stack = new Stack<treenode>();
        int result = root.val;
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                if (Math.abs(root.val - target) < Math.abs(result - target)) {
                    result = root.val;
                }
                root = root.right;
            }
        }
        return result;
    }
}
</treenode></treenode></pre>
<p>[/expand]</p>
