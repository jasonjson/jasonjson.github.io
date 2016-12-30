---
layout: post
title: Sort Colors II
date: 2015-10-21 14:38:05.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1455296169;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:573;}i:1;a:1:{s:2:"id";i:45;}i:2;a:1:{s:2:"id";i:443;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.</em></strong></p>
<p>[expand title = "code"]</p>
<pre>
class Solution {
    public void sortColors2(int[] colors, int k) {
        if (colors == null || colors.length == 0) return;
        
        int left = 0, right = colors.length - 1;
        for (int round = 0; round < k / 2; round++) {
            int red = round + 1, black = k - round;
            for (int i = left; i <= right; i++) {
                if (colors[i] == red) {
                    colors[i] = colors[left];
                    colors[left++] = red;
                } else if (colors[i] == black) {
                    colors[i] = colors[right];
                    colors[right--] = black;
                    i--;
                }
            }
        }
    }
}

</pre>
<p>[/expand]</p>
<p>[expand title="count sort"]</p>
<pre>
class Solution {
    /**
     * @param colors: A list of integer
     * @param k: An integer
     * @return: nothing
     */
    public void sortColors2(int[] colors, int k) {
        // write your code here
        if (colors == null || colors.length == 0) return;
        int[] table = new int[k + 1];
        //index - color, value - count of color
        for (int color : colors) {
            table[color] ++;
        }
        int index = 0;
        for (int i = 1; i <= k; i++) {
            while(table[i] > 0) {
                colors[index ++] = i;
                table[i] --;
            }
        }
    }
</pre>
<p>[/expand]</p>
