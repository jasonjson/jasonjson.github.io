---
layout: post
title: Binary Tree Preorder Traversal
date: 2015-10-21 02:49:50.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467188698;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:254;}i:1;a:1:{s:2:"id";i:252;}i:2;a:1:{s:2:"id";i:1193;}}}}
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
    public List<integer> preorderTraversal(TreeNode root) {
        List<integer> result = new ArrayList<integer>();
        if (root != null) {
            List<integer> left = preorderTraversal(root.left);
            List<integer> right = preorderTraversal(root.right);
            result.add(root.val);
            result.addAll(left);
            result.addAll(right);
        }
        return result;
    }
    //iterative!
    public ArrayList<integer> preorderTraversal(TreeNode root) {
        // write your code here
        ArrayList<integer> result = new ArrayList<integer>();
        if (root == null) {
            return result;
        }
        Stack<treenode> stack = new Stack<treenode>();
        stack.push(root);
        while (!stack.isEmpty()){
            TreeNode node = stack.pop();
            result.add(node.val); 
            //push right node first, which comes out later
            if (node.right != null) stack.push(node.right);
            if (node.left != null) stack.push(node.left);
        }
        return result;
    }
}
</treenode></treenode></integer></integer></integer></integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
