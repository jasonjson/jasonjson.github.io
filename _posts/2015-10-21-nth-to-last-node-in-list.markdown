---
layout: post
title: Nth to Last Node in List
date: 2015-10-21 03:01:39.000000000 -04:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
<p><strong><em>Find the nth to last element of a singly linked list. The minimum number of nodes in list is n.</em></strong></p>


``` java
public class Solution {
    /**
     * @param head: The first node of linked list.
     * @param n: An integer.
     * @return: Nth to last node of a singly linked list. 
     */
    ListNode nthToLast(ListNode head, int n) {
        // write your code here
        if (head == null) return null;
        
        ListNode fast = head, slow = head;
        for (int i = 0; i < n; i++) {
           fast = fast.next; 
        }
        
        while(fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
        return slow;
        // 3 - 4 - 5 - 6, n = 2
        // result should be 5 not 4
    }
}
```
