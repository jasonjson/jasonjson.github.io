---
layout: post
title: Convert Binary Search Tree to Doubly Linked List
date: 2015-10-27 15:22:08.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
- Data Structure
author: Jason
---
<p><strong><em>Convert a binary search tree to doubly linked list with in-order traversal.</em></strong></p>


``` java
public class Solution {
    /**
     * @param root: The root of tree
     * @return: the head of doubly list node
     */
    public DoublyListNode bstToDoublyList(TreeNode root) {  
        // Write your code here
        if (root == null) return null;
        ArrayList<Integer> list = new ArrayList<Integer>();
        Stack<treenode> stack = new Stack<treenode>();
        while (root != null) {
            stack.push(root);
            root = root.left;
        }
        while (!stack.isEmpty()) {
            TreeNode curr = stack.pop();
            list.add(curr.val);
            if (curr.right != null) {
                curr = curr.right;
                while (curr != null) {
                    stack.push(curr);
                    curr = curr.left;
                }
            }
        }
        DoublyListNode dummy = new DoublyListNode(0);
        DoublyListNode curr = dummy;
        DoublyListNode prev = null;
        for (int n : list) {
            curr.next = new DoublyListNode(n);
            curr.prev = prev;
            prev = curr;
            curr = curr.next;
        }
        return dummy.next;
    }
}
```
