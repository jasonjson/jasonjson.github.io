---
layout: post
title: Binary Search Tree Iterator
date: 2015-10-21 03:00:24.000000000 -04:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465224910;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:596;}i:1;a:1:{s:2:"id";i:1085;}i:2;a:1:{s:2:"id";i:268;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Design an iterator over a binary search tree with the following rules: Elements are visited in ascending order (i.e. an in-order traversal) next() and hasNext() queries run in O(1) time in average.</em></strong><br />
[expand title="code"]</p>
<pre>
public class BSTIterator {
    Stack<treenode> stack = new Stack<treenode>();
    public BSTIterator(TreeNode root) {
        if (root == null) return;
        while (root != null) {
            stack.push(root);
            root = root.left;
        }
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    /** @return the next smallest number */
    public int next() {
        TreeNode curr = stack.pop();
        int result = curr.val;
        if (curr.right != null) {
            curr = curr.right;
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
        }
        return result;
    }
}
</treenode></treenode></pre>
<p>[/expand]</p>
