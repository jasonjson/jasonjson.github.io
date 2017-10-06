---
layout: post
title: 147 - Insertion Sort List
date: 2015-10-21 02:48:46.000000000 -04:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
**Sort a linked list using insertion sort.**


``` java
public class Solution {
    /**
     * @param head: The first node of linked list.
     * @return: The head of linked list.
     */
    public ListNode insertionSortList(ListNode head) {
        // write your code here
        if (head == null) return null;
        ListNode dummy = new ListNode(0);

        while (head != null) {
            ListNode prev = dummy;
            while (prev.next != null && prev.next.val < head.val) {
            //bug: prev != null, prev = dummy, it's not null
                prev = prev.next;
            }
            //find the prev that is smaller than curr.val until the next is bigger than curr.val, and this is the place we need to insert curr
            ListNode next = head.next;
            //insert the node between prev and prev.next
            //draw a figure to help understand
            head.next = prev.next;
            prev.next = head;
            head = next;
        }
        return dummy.next;
    }
}
```

``` python
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return

        dummy = ListNode(0)
        while head:
            prev = dummy
            while prev.next and prev.next.val < head.val:
                prev = prev.next
            next_head = head.next
            head.next = prev.next
            prev.next = head
            head = next_head
        return dummy.next
```
