---
layout: post
title: Validate Binary Search Tree
date: 2015-10-21 02:58:13.000000000 -04:00
tags:
- Algorithm
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary tree, determine if it is a valid binary search tree (BST).</em></strong></p>


``` java
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
```

``` java
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
```
