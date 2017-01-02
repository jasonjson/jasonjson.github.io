---
layout: post
title: Check if a singly linked list is palindrome
date: 2015-10-21 02:48:25.000000000 -04:00
categories:
- LinkedList
- Palindrome
author: Jason
---
<p><strong><em>Given a singly linked list of integers, write a function that returns true if the given list is palindrome, else false.</em></strong><br />


``` java
class Solution {
    //we can also find the mid element, reverse the right part and compare with left part
    public static boolean isPalin(ListNode head) {
        if (head == null) return false;
        ListNode fast = head, slow = head;
        Stack<listnode> stack = new Stack<listnode>();
        while (fast != null && fast.next != null) {
            stack.push(slow);
            slow = slow.next;
            fast = fast.next.next;
        }

        if (fast != null) {
            slow = slow.next;
        } // if the number of elements is odd, ignore mid element

        while (slow != null) {
            int val = stack.pop().val;
            if (val != slow.val) {
                return false;
            }
            slow = slow.next;
        }
        return true;
    }
};
```
