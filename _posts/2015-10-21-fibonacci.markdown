---
layout: post
title: Fibonacci
date: 2015-10-21 02:38:49.000000000 -04:00
type: post
published: true
status: publish
categories:
- Dynamic Programming
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1458967182;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:107;}i:1;a:1:{s:2:"id";i:2071;}i:2;a:1:{s:2:"id";i:206;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Find the Nth number in Fibonacci sequence. A Fibonacci sequence is defined as follow: The first two numbers are 0 and 1. The ith number is the sum of i-1th number and i-2 th number.</em></strong><br />
[expand title="code"]</p>
<pre>
class Solution {
    /**
     * @param n: an integer
     * @return an integer f(n)
     */
    
    public static HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
    //create a static hashmap to be used during recursion
    public int fibonacci(int n) {
        if (n <= 0) return -1;
        if (n == 1) return 0;
        if (n == 2) return 1;
        if (map.containsKey(n)) {
            return map.get(n);
        }
        int result = fibonacci(n-1) + fibonacci(n-2);
        map.put(n, result);
        return result;
    }
}
</pre>
<p>[/expand]</p>
