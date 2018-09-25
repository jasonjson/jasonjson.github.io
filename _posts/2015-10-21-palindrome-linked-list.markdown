---
layout: post
title: 234 - Palindrome Linked List
date: 2015-10-21 14:45:44.000000000 -04:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
**Implement a function to check if a linked list is a palindrome.**


``` java
public class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;

        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        slow = reverse(slow);
        while (slow != null) {
            if (head.val != slow.val) {
                return false;
            }
            slow = slow.next;
            head = head.next;
        }
        return true;
    }
    public ListNode reverse(ListNode head) {
        ListNode rev = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = rev;
            rev = head;
            head = next;
        }
        return rev;
    }
}
```

``` python
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        slow = self.reverse(slow)
        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True

    def reverse(self, node):
        rev = None
        while node:
            next_node = node.next
            node.next = rev
            rev = node
            node = next_node
        return rev
```
