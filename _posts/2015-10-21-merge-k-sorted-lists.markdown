---
layout: post
title: Merge k Sorted Lists
date: 2015-10-21 02:47:17.000000000 -04:00
type: post
published: true
status: publish
categories:
- LinkedList
- Sorting
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464846170;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1848;}i:1;a:1:{s:2:"id";i:246;}i:2;a:1:{s:2:"id";i:234;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.</em></strong><br />
[expand title="code"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
