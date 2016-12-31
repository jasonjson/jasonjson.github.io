---
layout: post
title: Closest Binary Search Tree Value II
date: 2015-10-30 11:29:11.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469289896;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1198;}i:1;a:1:{s:2:"id";i:2079;}i:2;a:1:{s:2:"id";i:333;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.</em></strong><br />
Note:<br />
Given target value is a floating point.<br />
You may assume k is always valid, that is: k ≤ total nodes.<br />
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.</p>
<p>Follow up:<br />
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)? Divide and conquer, get the result from left subtree and right subtree then merge</p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public List<integer> closestKValues(TreeNode root, double target, int k) {
        List<integer> result = new ArrayList<integer>();
        if (root == null) return result;
        
        Stack<treenode> stack = new Stack<treenode>();
        while (!stack.isEmpty() || root != null) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                if (result.size() < k) {
                    result.add(root.val);
                } else if (Math.abs(root.val - target) < Math.abs(result.get(0) - target)) {
                    result.remove(0);
                    result.add(root.val);
                } else {//后面的数更大 不需要考虑 关键是找到中间k个数
                    break;
                }
                root = root.right;
            }
        }
        return result;
    }
}
</treenode></treenode></integer></integer></integer></pre>
<p>[/expand]</p>
