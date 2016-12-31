---
layout: post
title: Insertion Sort List
date: 2015-10-21 02:48:46.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469291627;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:592;}i:1;a:1:{s:2:"id";i:601;}i:2;a:1:{s:2:"id";i:246;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Sort a linked list using insertion sort.</em></strong><br />
[expand title="code"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
