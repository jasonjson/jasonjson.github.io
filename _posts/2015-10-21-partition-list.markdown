---
layout: post
title: Partition List
date: 2015-10-21 02:44:06.000000000 -04:00
tags:
- Algorithm
categories:
- LinkedList
author: Jason
---
<p><strong><em>Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x. You should preserve the original relative order of the nodes in each of the two partitions.</em></strong></p>


``` java
public class Solution {
    /**
     * @param head: The first node of linked list.
     * @param x: an integer
     * @return: a ListNode
     */
    public ListNode partition(ListNode head, int x) {
        // write your code here
        if (head == null) return null;
        ListNode leftDummy = new ListNode(0);
        ListNode left = leftDummy;
        ListNode rightDummy = new ListNode(0);
        ListNode right = rightDummy;
        ListNode curr = head;
        while (curr != null) {
            if (curr.val < x) {
                left.next = curr;
                left = left.next;
            } else {
                right.next = curr;
                right = right.next;
            }
            curr = curr.next;
        }
        right.next = null;
        //bug: forget to clear the right.next, which causes an infinity loop
        //in the end, right.next = curr, and curr has its own next node, you need to clear this node.
        left.next = rightDummy.next;
        return leftDummy.next;
    }
}
```
``` python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left_dummy, right_dummy = ListNode(0), ListNode(0)
        left, right = left_dummy,right_dummy
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        right.next = None
        left.next = right_dummy.next
        return left_dummy.next
```
