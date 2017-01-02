---
layout: post
title: Palindrome Linked List
date: 2015-10-21 14:45:44.000000000 -04:00
categories:
- LinkedList
- Palindrome
author: Jason
---
<p><strong><em>Implement a function to check if a linked list is a palindrome.</em></strong></p>

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
        if (fast != null) {
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
