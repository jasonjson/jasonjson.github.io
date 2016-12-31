---
layout: post
title: Permutation index
date: 2015-10-21 03:38:04.000000000 -04:00
type: post
published: true
status: publish
categories:
- DFS Backtracking
- Permutation
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468324630;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:341;}i:1;a:1:{s:2:"id";i:109;}i:2;a:1:{s:2:"id";i:1058;}}}}
  _inbound_impressions_count: '0'
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a permutation which contains no repeated number, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.</em></strong><br />
<a href="http://algorithm.yuanbin.me/zh-cn/exhaustive_search/permutation_index.html">See explanations here</a><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param A an integer array
     * @return a long integer
     */
    public long permutationIndex(int[] A) {
        if (A.length == 0 || A == null) return 0;
        
        long index = 1, factor = 1;
        for (int i = A.length - 1; i >= 0; i--) {
            //从右边开始只是为了便于计算factorial
            int rank = 0;
            for (int j = i + 1; j < A.length; j++) {
                if (A[i] > A[j]) rank ++;
            }//找到i右边比A[i]小的数,从而计算把A[i]与之互换可能产生的index更小的permutation,
            index += rank * factor;
            factor *= A.length - i;
        }
        return index;
    }
}
</pre>
<p>[/expand]</p>
