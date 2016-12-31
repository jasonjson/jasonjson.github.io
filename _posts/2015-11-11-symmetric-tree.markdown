---
layout: post
title: Symmetric Tree
date: 2015-11-11 17:24:07.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464400708;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:596;}i:1;a:1:{s:2:"id";i:278;}i:2;a:1:{s:2:"id";i:254;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).</em></strong></p>
<p>[expand title="recursion"]</p>
<pre>
public class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return helper(root, root);
    }
    
    public boolean helper(TreeNode a, TreeNode b) {
        if (a == null && b == null) return true;
        if (a == null || b == null) return false;
        return a.val == b.val && helper(a.left, b.right) && helper(a.right, b.left);
    }
}
</pre>
<p>[/expand]<br />
[expand title="iterative"]</p>
<pre>
public class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        Queue<treenode> q1 = new LinkedList<treenode>();
        Queue<treenode> q2 = new LinkedList<treenode>();
        q1.offer(root);
        q2.offer(root);
        while (!q1.isEmpty() && !q2.isEmpty()) {
            TreeNode left = q1.poll();
            TreeNode right = q2.poll();
            if (left == null && right == null) continue;
            if (left == null || right == null || left.val != right.val) return false;
            q1.offer(left.left);
            q1.offer(left.right);
            q2.offer(right.right);
            q2.offer(right.left);
        }
        return q1.size() == q2.size();
    }
}
</treenode></treenode></treenode></treenode></pre>
<p>[/expand]</p>
