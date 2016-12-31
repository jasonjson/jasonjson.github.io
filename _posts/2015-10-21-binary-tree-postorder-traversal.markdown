---
layout: post
title: Binary Tree Postorder Traversal
date: 2015-10-21 02:50:25.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469019801;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:284;}i:1;a:1:{s:2:"id";i:252;}i:2;a:1:{s:2:"id";i:1470;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p>[expand title = "iterative"]</p>
<pre>
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: Postorder in ArrayList which contains node values.
     */
    public ArrayList<integer> postorderTraversal(TreeNode root) {
        // write your code here
        ArrayList<integer> result = new ArrayList<integer>();
        if (root == null) return result;
        
        Stack<treenode> stack = new Stack<treenode>();
        TreeNode prev = null;
        stack.push(root);
        while (!stack.isEmpty()) {
            root = stack.peek();
            boolean nochildren = false;
            if (root.left == null && root.right == null) {
                nochildren = true;
            }
            boolean childrenvisited = false;
            if (prev != null && (root.left == prev || root.right == prev)) {
                childrenvisited = true;
            }
            if (nochildren || childrenvisited) {
                prev = stack.pop();
                result.add(root.val);
            } else {
                if (root.right != null) {
                    stack.push(root.right);
                }
                if (root.left != null) {
                    stack.push(root.left);
                }
            }
        }
        return result;
    }
}
</treenode></treenode></integer></integer></integer></pre>
<p>[/expand]</p>
<p>[expand title="recursive"]</p>
<pre>
public class Solution {
    public ArrayList<integer> postorderTraversal(TreeNode root) {
        // write your code here
        ArrayList<integer> result = new ArrayList<integer>();
        if (root != null) {
            ArrayList<integer> left = postorderTraversal(root.left);
            ArrayList<integer> right = postorderTraversal(root.right);
            result.addAll(left);
            result.addAll(right);
            result.add(root.val);
        }
        return result;
    }
}
</integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
