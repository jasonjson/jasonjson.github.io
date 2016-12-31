---
layout: post
title: Flatten Binary Tree to Linked List
date: 2015-10-21 14:43:36.000000000 -04:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
- LinkedList
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469155047;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1085;}i:1;a:1:{s:2:"id";i:268;}i:2;a:1:{s:2:"id";i:292;}}}}
  _inbound_impressions_count: '0'
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Flatten a binary tree to a fake "linked list" in pre-order traversal. Here we use the right pointer in TreeNode as the next pointer in ListNode.</em></strong></p>
<p>[expand title = "iterative"]</p>
<pre>
public class Solution {
    public void flatten(TreeNode root) {
        if (root == null) return;
        
        Stack<treenode> stack = new Stack<treenode>();
        stack.push(root);
        TreeNode prev = null;
        while (!stack.isEmpty()) {
            TreeNode curr = stack.pop();
            if (prev != null) {
                prev.right = curr;
                prev.left = null;
            }
            prev = curr;
            if (curr.right != null) {
                stack.push(curr.right);
            }
            if (curr.left != null) {
                stack.push(curr.left);
            }
        }
    }
}
</treenode></treenode></pre>
<p>[/expand]</p>
<p>[expand title="recursive"]</p>
<pre>
public class Solution {
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void flatten(TreeNode root) {
        // write your code here
        if (root == null) return;
        helper(root);
    }
    public TreeNode helper(TreeNode root) {
        if (root == null) return null;
        TreeNode left = helper(root.left);
        TreeNode right = helper(root.right);
        root.left = null;
        root.right = left;
        TreeNode curr = root;
        while (curr.right != null) {
            curr = curr.right;
        }
        curr.right = right;
        return root;
    }
}
</pre>
<p>[/expand]</p>
