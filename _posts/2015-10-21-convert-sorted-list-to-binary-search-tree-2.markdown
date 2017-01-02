---
layout: post
title: Convert Sorted List to Binary Search Tree
date: 2015-10-21 03:00:01.000000000 -04:00
categories:
- Binary Search Tree
- LinkedList
author: Jason
---
<p><strong><em>Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.</em></strong><br />


``` java
public class Solution {
    /**
     * @param head: The first node of linked list.
     * @return: a tree node
     */
    public TreeNode sortedListToBST(ListNode head) {  
        // write your code here
        if (head == null) return null;
        ListNode right = head, fast = head, prev = null;
        while (fast != null && fast.next != null) {
            prev = right;
            right = right.next;
            fast = fast.next.next;
        }
        TreeNode root = new TreeNode(right.val);
        if (prev != null) {//一定要单独考虑prev == null的情况
            prev.next = null;
            root.left = sortedListToBST(head);
            root.right = sortedListToBST(right.next);
        } 
        return root;
    }
}
```

``` java
public class Solution {
    public static ListNode h;
    public TreeNode sortedListToBST(ListNode head) { 
        if (head == null) return null;
        if (head.next == null) return new TreeNode(head.val);
        h = head;
        int len = 0;
        while (head != null) {
            head = head.next;
            len ++;
        }
        return sortedListToBSTUtil(0, len - 1);
    }    
    public TreeNode sortedListToBSTUtil(int start, int end) {
        if (start > end) return null;
        int mid = start + (end - start) / 2;
        TreeNode leftChild = sortedListToBSTUtil(start, mid - 1);
        TreeNode root = new TreeNode(h.val);
        h = h.next;
        root.left = leftChild;
        root.right = sortedListToBSTUtil(mid + 1, end);
        return root;
    }
}
```
