---
layout: post
title: Divide Two Integers
date: 2015-10-21 14:04:10.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
tags: []
meta:
  _wpas_done_all: '1'
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466022381;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:536;}i:1;a:1:{s:2:"id";i:553;}i:2;a:1:{s:2:"id";i:466;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Divide two integers without using multiplication, division and mod operator. If it is overflow, return 2147483647</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param dividend the dividend
     * @param divisor the divisor
     * @return the result
     */
    public int divide(int dividend, int divisor) {
        // Write your code here
        boolean positive = true;
        if ((dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0)) {
            positive = false;
        }
        long dvd = Math.abs((long)dividend);//先转化成long再求绝对值
        long dvs = Math.abs((long)divisor);
        
        long result = helper(dvd, dvs);
        if (result >= Integer.MAX_VALUE) {
            return positive ? Integer.MAX_VALUE : Integer.MIN_VALUE;
        }
        return positive ? (int) result : -(int)result;
    }
    
    public long helper(long dvd, long dvs) {
        if (dvd < dvs) return 0;
        long sum = dvs, multiple = 1;
        while (sum + sum <= dvd) {
            sum += sum;
            multiple += multiple;
        }
        return multiple + helper(dvd - sum, dvs);
    }
}
</pre>
<p>[/expand]</p>
