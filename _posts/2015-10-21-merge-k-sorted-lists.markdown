---
layout: post
title: Merge k Sorted Lists
date: 2015-10-21 02:47:17.000000000 -04:00
categories:
- LinkedList
- Sorting
author: Jason
---
<p><strong><em>Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.</em></strong><br />


``` java
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0 || lists == null) return null;
        return mergeKListsUtil(lists, 0, lists.length - 1);
    }
    
    public ListNode mergeKListsUtil(ListNode[] lists, int lo, int hi) {
        if (lo == hi) {
            return lists[lo];
        }
        ListNode left = mergeKListsUtil(lists, lo, lo + (hi - lo) / 2);
        ListNode right = mergeKListsUtil(lists, lo + (hi - lo) / 2 + 1, hi);
        return mergeTwoLists(left, right);
    }
    
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        curr.next = l1 == null ? l2 : l1;
        return dummy.next;
    }
}
```
