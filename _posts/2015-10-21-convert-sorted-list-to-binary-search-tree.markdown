---
layout: post
title: 109 - Convert Sorted List to Binary Search Tree
date: 2015-10-21 03:00:01.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
- LinkedList
author: Jason
---
**Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.**


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
``` python
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        if not head:
            return

        prev, right, fast = None, head, head
        while fast and fast.next:
            prev = right
            right = right.next
            fast = fast.next.next

        root = TreeNode(right.val)
        if prev:
            prev.next = None
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(right.next)
        return root
```
