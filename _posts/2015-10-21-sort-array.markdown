---
layout: post
title: Sort array
date: 2015-10-21 02:09:22.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1455545613;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:149;}i:1;a:1:{s:2:"id";i:936;}i:2;a:1:{s:2:"id";i:139;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given sorted array of doubles, return the another sorted array of doubles where all elements are the squares from the input array.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Sort {
    public int[] getSorted(int[] arr){
        int n = arr.length;
        int[] result = new int[n];
        int lo = 0, hi = n - 1, k = n - 1;
        while (lo < hi) {
            int n1 = arr[lo] * arr[lo];
            int n2 = arr[hi] * arr[hi];
            if(n1 >= n2) {
                result[k--] = n1;
                lo++;
            } else {
                result[k--] = n2;
                hi--;
            }
        }
        return result;
    }
}
</pre>
<p>[/expand]</p>
