---
layout: post
title: Remove Duplicates from Sorted List II
date: 2015-10-21 02:43:18.000000000 -04:00
tags:
- Algorithm
categories:
- LinkedList
author: Jason
---
**Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.**


``` java
public class Solution {
    /**
     * @param ListNode head is the head of the linked list
     * @return: ListNode head of the linked list
     */
    public static ListNode deleteDuplicates(ListNode head) {
        // write your code here
        if (head == null) return null;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode curr = dummy;
        while (curr.next != null && curr.next.next != null) {
            if (curr.next.val == curr.next.next.val) {
                int prev_val = curr.next.val;
                //store the same value
                while (curr.next != null && curr.next.val == prev_val) {
                    //if the value is the same, we redirect the curr node
                    curr.next = curr.next.next;
                }
            } else {
                curr = curr.next;//do not move curr until the next two nodes are different
            }
        }
        return dummy.next;
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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                repeated_value = curr.next.val
                while curr.next and curr.next.val == repeated_value:
                    curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
```
