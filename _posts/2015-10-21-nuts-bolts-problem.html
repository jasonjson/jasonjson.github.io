---
layout: post
title: Nuts & Bolts Problem
date: 2015-10-21 13:08:03.000000000 -04:00
type: post
published: true
status: publish
categories:
- Sorting
tags: []
meta:
  _wpcom_is_markdown: '1'
  _wpas_done_all: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465148253;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1560;}i:1;a:1:{s:2:"id";i:443;}i:2;a:1:{s:2:"id";i:936;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a set of n nuts of different sizes and n bolts of different sizes. There is a one-one mapping between nuts and bolts. Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public void sortNutsAndBolts(String[] nuts, String[] bolts, NBComparator compare) {
        if (nuts == null || bolts == null) return;
        int m = nuts.length, n = bolts.length;
        if (m != n || m == 0 || n == 0) return;
        
        quickSort(nuts, bolts, compare, 0, m - 1);
    }    
    public void quickSort(String[] nuts, String[] bolts, NBComparator compare, int start, int end) {
        if (start >= end) return;
        int index = partition(nuts, bolts[start], compare, start, end);
        partition(bolts, nuts[index], compare, start, end);
        quickSort(nuts, bolts, compare, start, index - 1);
        quickSort(nuts, bolts, compare, index + 1, end);
    }
    public int partition(String[] strings, String pivot, NBComparator compare, int start, int end) {
        int index = start;//store for return value
        for (int i = start + 1; i <= end; i++) {
            if (compare.cmp(pivot, strings[i]) == 1 || compare.cmp(strings[i], pivot) == -1) {
                swap(strings, ++ index, i);//exchange small and large values
            } else if (compare.cmp(pivot, strings[i]) == 0 || compare.cmp(strings[i], pivot) == 0) {
                swap(strings, start, i); 
                //put strings[i] with real pivot value to start position 
                i--;//the value used to be in start index, which is not checked yet
            }
        }
        swap(strings, index, start);//put pivot to the correct index 
        return index;
    }
    public void swap(String[] strings, int a, int b) {
        String temp = strings[a];
        strings[a] = strings[b];
        strings[b] = temp;
    }
};//http://algorithm.yuanbin.me/zh-cn/problem_misc/nuts_and_bolts_problem.html
</pre>
<p>[/expand]</p>
