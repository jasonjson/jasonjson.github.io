---
layout: post
title: Convert Sorted List to Binary Search Tree
date: 2015-10-21 01:44:02.000000000 -04:00
tags: algorithm
categories:
- Binary Search Tree
- LinkedList
- Binary search tree
- LinkedList
author: Jason
---
<p><strong><em>Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.</em></strong></p>


``` java
    /**
     * @param head: The first node of linked list.
     * @return: a tree node
     */
     
    public static ListNode h; //static variable
    public TreeNode sortedListToBST(ListNode head) {  
        // write your code here/
        int count = 0;
        h = head;
        ListNode runner = head;
        while(runner != null){
            count ++;
            runner = runner.next;
        }//get length of the Linkedlist
        return sortedListToBST(0, count - 1);
        
    }
    public TreeNode sortedListToBST(int lo, int hi){
        if(lo > hi) return null;
        int mid = (lo + hi) / 2;
        //like inorder traversal, start from the left child to root to right child
        TreeNode leftChild = sortedListToBST(lo, mid - 1);
        TreeNode root = new TreeNode(h.val);
        root.left = leftChild;
        h = h.next;
        root.right = sortedListToBST(mid + 1, hi);
        return root;
    }
}
```
