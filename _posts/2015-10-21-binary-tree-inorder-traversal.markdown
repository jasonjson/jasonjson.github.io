---
layout: post
title: Binary Tree Inorder Traversal
date: 2015-10-21 02:50:09.000000000 -04:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464218973;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:254;}i:1;a:1:{s:2:"id";i:250;}i:2;a:1:{s:2:"id";i:258;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: Inorder in ArrayList which contains node values.
     */
    public ArrayList<integer> inorderTraversal(TreeNode root) {
        ArrayList<integer> result = new ArrayList<integer>();
        if (root != null) {
            ArrayList<integer> left = inorderTraversal(root.left);
            ArrayList<integer> right = inorderTraversal(root.right);
            result.addAll(left);
            result.add(root.val);
            result.addAll(right);
        }
        return result;
    }
    //iterative
    public ArrayList<integer> inorderTraversal(TreeNode root) {
        ArrayList<integer> result = new ArrayList<integer>();
        Stack<treenode> stack = new Stack<treenode>();
        
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                //when root gets to null, pop the stack and move to the right child
                root = stack.pop();
                result.add(root.val);
                root = root.right;
            }
        }
        return result;
    }
}
</treenode></treenode></integer></integer></integer></integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
