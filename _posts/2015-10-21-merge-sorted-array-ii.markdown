---
layout: post
title: Merge Sorted Array II
date: 2015-10-21 02:25:04.000000000 -04:00
type: post
published: true
status: publish
categories:
- Sorting
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467212940;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:45;}i:1;a:1:{s:2:"id";i:936;}i:2;a:1:{s:2:"id";i:1758;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Merge two given sorted integer array A and B into a new sorted integer array.</em></strong><br />
[expand title="code"]</p>
<pre>
class Solution {
    /**
     * @param A and B: sorted integer array A and B.
     * @return: A new sorted integer array
     */
    public ArrayList<integer> mergeSortedArray(ArrayList<integer> A, ArrayList<integer> B) {
        // write your code here
        ArrayList<integer> C = new ArrayList<integer>();
        while (!A.isEmpty() && !B.isEmpty()){
            if (A.get(0) <= B.get(0)) C.add(A.remove(0));
            else C.add(B.remove(0));
        }
        while (!A.isEmpty()){
            C.add(A.remove(0));
        }
        while (!B.isEmpty()){
            C.add(B.remove(0));
        }
        return C;
    }
}
</integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
