---
layout: post
title: Unique Binary Search Trees II
date: 2015-10-21 03:40:35.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465511660;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:272;}i:1;a:1:{s:2:"id";i:1058;}i:2;a:1:{s:2:"id";i:1193;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @paramn n: An integer
     * @return: A list of root
     */
    public List<treenode> generateTrees(int n) {
        // write your code here
        return generateTreesUtil(1, n);
    }
    
    public List<treenode> generateTreesUtil(int start, int end) {
        List<treenode> result = new ArrayList<treenode>();
        if (start > end) {
            result.add(null); //must deal with null TreeNode here, otherwise fail for n = 1
            return result;
        }
        for (int i = start; i <= end; i++) {//use i as root to construct BST
        //create all possible left subtree roots and right subtree roots
            List<treenode> leftTree = generateTreesUtil(start, i - 1);
            List<treenode> rightTree = generateTreesUtil(i + 1, end);
            for (TreeNode leftroot : leftTree) {
                for (TreeNode rightroot : rightTree) {
                //connect root to all possible subtree roots
                    TreeNode root = new TreeNode(i);
                    root.left = leftroot;
                    root.right = rightroot;
                    result.add(root);
                }
            }
        }
        return result;
    }
}
</treenode></treenode></treenode></treenode></treenode></treenode></pre>
<p>[/expand]</p>
