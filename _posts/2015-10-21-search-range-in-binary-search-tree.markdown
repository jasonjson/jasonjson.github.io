---
layout: post
title: Search Range in Binary Search Tree
date: 2015-10-21 02:58:42.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given two values k1 and k2 (where k1 &lt; k2) and a root pointer to a Binary Search Tree. Find all the keys of tree in range k1 to k2. i.e. print all x such that k1&lt;=x&lt;=k2 and x is a key of given BST. Return all the keys in ascending order.</em></strong></p>


``` java
public class Solution {
    /**
     * @param root: The root of the binary search tree.
     * @param k1 and k2: range k1 to k2.
     * @return: Return all keys that k1<=key<=k2 in ascending order.
     */
    public ArrayList<Integer> searchRange(TreeNode root, int k1, int k2) {
        // write your code here
        ArrayList<Integer> array = new ArrayList<Integer>();
        inorderTraversal(root, array);
        ArrayList<Integer> result = new ArrayList<Integer>();
        for(int i = 0; i < array.size(); i++){
            int val = array.get(i);
            if(val >= k1 && val <= k2) result.add(val);
        }
        return result;
    }   
    public void inorderTraversal(TreeNode root, ArrayList<Integer> array){
        if(root == null) return;
        inorderTraversal(root.left, array);
        array.add(root.val);
        inorderTraversal(root.right, array);
    }
    //Solution 2, add value while traversal, and only add elements in the range
    public ArrayList<Integer> searchRange(TreeNode root, int k1, int k2) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        helper(root, k1, k2, result);
        return result;
    }   
    public void helper(TreeNode root, int k1, int k2, ArrayList<Integer> result){
        if (root == null) return; 
        三个if是并存的关系，不是if else，表示我们三个点是否都需要查找       
        if (root.val > k1) { 
            helper(root.left, k1, k2, result);
        }//if root.val <= k1, there left subtree won't have elements in range
        if (root.val >= k1 && root.val <= k2) {
            result.add(root.val);
        }//if root.val >= k2, then right subtree won't have elements in range        
        if (root.val < k2) {
            helper(root.right, k1, k2, result);
        }//the way we write three ifs make sure the value in the arraylist is ascending
    }
}
```
