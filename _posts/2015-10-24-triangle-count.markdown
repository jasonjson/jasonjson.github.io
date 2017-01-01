---
layout: post
title: Triangle Count
date: 2015-10-24 12:06:43.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Matrix
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465398958;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1208;}i:1;a:1:{s:2:"id";i:347;}i:2;a:1:{s:2:"id";i:2071;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle whose three edges length is the three numbers that we find?</em></strong></p>
<p>[expand title="DFS"]</p>
<pre>
public class Solution {
    /**
     * @param S: A list of integers
     * @return: An integer
     */
    public static Integer count = 0;
    public int triangleCount(int S[]) {
        // write your code here
        if (S == null || S.length == 0) return 0;
        
        Arrays.sort(S);
        List<integer> list = new ArrayList<integer>();
        helper(S, 0, list);
        return count;
    }
    
    public void helper(int[] S, int start, List<integer> list) {
        if (list.size() == 3 && isTri(list)) {
            count ++;
            return;
        }
        for (int i = start; i < S.length; i++) {
            int c = S[i];
            if (list.size() == 2) {
                int a = list.get(0), b = list.get(1);
                if (a + b < c || c - b > a || c - a > b) {
                    break;
                }
            }
            list.add(c);
            helper(S, i + 1, list);
            list.remove(list.size() - 1);
        }
    }
    
    public boolean isTri(List<integer> list) {
        Collections.sort(list);
        int a = list.get(0), b = list.get(1), c = list.get(2);
        if (a + b > c && b - a < c && c - a < b && c - b < a) {
            return true;
        } else {
            return false;
        }
    }
}
</integer></integer></integer></integer></pre>
<p>[/expand]</p>
<p>[expand title = "Two pointers"]</p>
<pre>
public class Solution {
    /**
     * @param S: A list of integers
     * @return: An integer
     */
    public int triangleCount(int S[]) {
        // write your code here
        if (S == null || S.length == 0) return 0;
        
        int count = 0;
        Arrays.sort(S);
        for (int end = S.length - 1; end >= 2; end --) {
            //S[end] 为最大的边
            int start = 0, mid = end - 1;
            while (start < mid) {
                if (S[start] + S[mid] <= S[end]) {
                    start ++;//不满足条件 左边界缩进
                } else {
                    count += mid - start;//最小的A[start]都满足条件，则中间所有的元素都可以作为最小的边，满足条件
                    mid --;//A[mid] 第二大边
                }
            }
        }
        return count;
    }
}
</pre>
<p>[/expand]</p>
