---
layout: post
title: Subarray Sum K
date: 2015-10-21 02:17:46.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467223994;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:105;}i:1;a:1:{s:2:"id";i:466;}i:2;a:1:{s:2:"id";i:499;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an nonnegative integer array, find a subarray where the sum of numbers is k. Your code should return the index of the first number and the index of the last number.</em></strong><br />
[expand title="code"]</p>
<pre>
public class solution {
    public static void main(String[] args) {
        int[] a = {1, 4, 0, 0, 3, 10, 5};;
        ArrayList<integer> list = findSum(a,7);
        for(int n : list){
            System.out.println(n);
        }
    }

    public static ArrayList<integer> findSum(int[] arr, int val){
        if(arr == null) return null;
        HashMap<Integer,Integer> map = new HashMap<Integer, Integer>();
        ArrayList<integer> result = new ArrayList<integer>();
        int sum = 0;
        for(int i = 0; i < arr.length; i++){
            sum += arr[i];
            if(sum == val){
                result.add(0);
                result.add(i);
                break;
            }else if(map.containsKey(sum-val)){
                result.add(map.get(sum-val) + 1);
                result.add(i);
                break;
            }else {
                map.put(sum,i);
            }
        }
        return result;
    }
}
</integer></integer></integer></integer></pre>
<p>[/expand]</p>
