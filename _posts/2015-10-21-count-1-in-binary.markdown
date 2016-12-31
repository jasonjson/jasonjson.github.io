---
layout: post
title: Count 1 in Binary
date: 2015-10-21 02:38:23.000000000 -04:00
type: post
published: true
status: publish
categories:
- Bit
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465433668;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:453;}i:1;a:1:{s:2:"id";i:109;}i:2;a:1:{s:2:"id";i:499;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Count how many 1 in binary representation of a 32-bit integer. follow up: Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).</em></strong></p>
<p><a href="http://www.java-samples.com/showtutorial.php?tutorialid=60">unsigned right shift</a><br />
[expand title = "unsigned"]</p>
<pre>
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count = 0;
        for (int i = 0; i < 32; i++) {
            if ((n & 1) == 1) {
                count ++;
            }
            n >>>= 1;
        }
        return count;
    }
}
</pre>
<p>[/expand]<br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param num: an integer
     * @return: an integer, the number of ones in num
     */
    public int countOnes(int num) {
        // write your code here
        //in case num is negative
        int count = 0;
        for (int i = 0; i < 32; i++) {
            if((num & 1) == 1) count ++; 
            // remember to put parentheses around (num & 1);
            num >>= 1;
            //bug: num >> 1, it's not a statement!!!!
        }
        return count;
    }
}
</pre>
<p>[/expand]</p>
