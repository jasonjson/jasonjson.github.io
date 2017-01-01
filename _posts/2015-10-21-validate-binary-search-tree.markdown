---
layout: post
title: Validate Binary Search Tree
date: 2015-10-21 02:58:13.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463620573;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:254;}i:1;a:1:{s:2:"id";i:286;}i:2;a:1:{s:2:"id";i:250;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a binary tree, determine if it is a valid binary search tree (BST).</em></strong><br />
[expand title="code1"]</p>
<pre>
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */
    public boolean isValidBST(TreeNode root) {
        // write your code here
        ArrayList<integer> array = new ArrayList<integer>();
        inorderTraversal(array, root);
        for(int i = 0; i < array.size() - 1; i++){
            if (array.get(i) >= array.get(i+1)) return false;
        }
        return true;
    }
    
    public void inorderTraversal(ArrayList<integer> array, TreeNode root){
        if(root == null) return;
        inorderTraversal(array, root.left);
        array.add(root.val);
        inorderTraversal(array, root.right);
    }
}
</integer></integer></integer></pre>
<p>[/expand]<br />
[expand title="code2"]</p>
<pre>
public class Solution {
    public static Integer lastPrinted;
    public boolean isValidBST(TreeNode root) {
        // write your code here
        if(root == null) return true;
        if(!isValidBST(root.left)) return false;
        if(lastPrinted != null && root.val <= lastPrinted) return false;
        lastPrinted = root.val;
        if(!isValidBST(root.right)) return false;
        return true;
    }
    //Solution 3: create a min and max value
}
</pre>
<p>[/expand]</p>
