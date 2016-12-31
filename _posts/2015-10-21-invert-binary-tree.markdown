---
layout: post
title: Invert Binary Tree
date: 2015-10-21 02:53:24.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463850874;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:596;}i:1;a:1:{s:2:"id";i:254;}i:2;a:1:{s:2:"id";i:284;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p>[expand title="code"]</p>
<pre>
***public class Solution {
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void invertBinaryTree(TreeNode root) {
        // write your code here
        if (root == null) return;
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        //from top to bottom
        invertBinaryTree(root.left);
        invertBinaryTree(root.right);
    }
    //iterative
    public void invertBinaryTree(TreeNode root) {
        // write your code here
        if (root == null) return;
        Stack<treenode> stack = new Stack<treenode>();
        
        stack.push(root);
        while (!stack.isEmpty()) {
            //we don't care if the current level is finished, when i level is finished, it goes automatically to i + 1 level, root remain the same, because it's already swapped in the above level
            TreeNode curr = stack.pop();
            TreeNode temp = curr.left;
            curr.left = curr.right;
            curr.right = temp;
            if (curr.left != null)  stack.push(curr.left);
            if (curr.right != null) stack.push(curr.right);
        }
    }
}
</treenode></treenode></pre>
<p>[/expand]</p>
