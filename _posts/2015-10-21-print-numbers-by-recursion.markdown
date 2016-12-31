---
layout: post
title: Print Numbers by Recursion
date: 2015-10-21 02:39:42.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1462964326;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:443;}i:1;a:1:{s:2:"id";i:107;}i:2;a:1:{s:2:"id";i:505;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Print numbers from 1 to the largest number with N digits by recursion.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param n: An integer.
     * return : An array storing 1 to the largest number with n digits.
     */
    public static List<integer> numbersByRecursion(int n) {
        // write your code here
        List<integer> result = new ArrayList<integer>();
        if (n <= 0) return result;

        result.add(0);//帮忙生成10, 20, 30....
        int base = 1;
        for (int i = 1; i <= n; i++) {
            int size = result.size();
            for (int k = 1; k <= 9; k++) {
                for (int j = 0; j < size; j++) {
                    //result.add(base); 0 + base * k !!
                    result.add(result.get(j) + base * k);
                }
            }
            base *= 10;
        }
        result.remove(0);
        return result;
    }
}
</integer></integer></integer></pre>
<p>[/expand]</p>
