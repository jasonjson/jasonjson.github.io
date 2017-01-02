---
layout: post
title: Unique Binary Search Trees II
date: 2015-10-21 03:40:35.000000000 -04:00
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.</em></strong><br />


``` java
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
```
