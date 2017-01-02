---
layout: post
title: Remove Duplicates from Unsorted List
date: 2015-10-21 02:43:44.000000000 -04:00
categories:
- LinkedList
author: Jason
---
<p><strong><em>Write a removeDuplicates() function which takes a list and deletes any duplicate nodes from the list. The list is not sorted.</em></strong></p>


``` java
class Solution {
    public static void main(String[] args) {
        ListNode l1 = new ListNode(1);
        ListNode l2 = new ListNode(2);
        ListNode l3 = new ListNode(2);
        ListNode l4 = new ListNode(2);
        ListNode l5 = new ListNode(3);
        ListNode l6 = new ListNode(4);
        l1.next = l2;
        l2.next = l3;
        l3.next = l4;
        l4.next = l5;
        l5.next = l6;
        ListNode head = remove(l1);
        while (head != null) {
            System.out.println(head.val);
            head = head.next;
        }
    }


    public static ListNode remove(ListNode head) {
        if (head == null) return null;
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        ListNode curr = head;
        map.put(curr.val,1); // don't forget to put the head value
        while (curr.next != null) {
            int val = curr.next.val;
            if (map.containsKey(val)) {
                curr.next = curr.next.next;
            } else {
                map.put(val, 1);
                curr = curr.next;
            }
        }
        return head;
    }
};
```
