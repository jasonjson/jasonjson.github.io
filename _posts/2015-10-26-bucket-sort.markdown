---
layout: post
title: Bucket sort
date: 2015-10-26 12:49:16.000000000 -04:00
type: post
published: true
status: publish
categories:
- Sorting
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1453433720;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1038;}i:1;a:1:{s:2:"id";i:2059;}i:2;a:1:{s:2:"id";i:1996;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Bucket sort an array.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public static void main(String[] args) {
        int[] A = {1,3,4,12,4,6,1,8};
        int[] B = bucketSort(A);
        for (int n : B) {
            System.out.print(n +",");
        }
    }
    public static int[] bucketSort(int[] A) {
        int max = A[0];
        for (int n : A) {
            max = Math.max(max, n);
        }
        int[] bucket = new int[max + 1];
        int[] sorted = new int[A.length];

        for (int n : A) {
            bucket[n] ++;
        }//one value in each bucket, bucket[i] stores the number of value n

        int index = 0;
        for (int i = 0; i < bucket.length; i++) {
            for (int j = 0; j < bucket[i]; j++) {//check how many duplicates
                sorted[index++] = i;
            }
        }
        return sorted;
    }
}
</pre>
<p>[/expand]</p>
