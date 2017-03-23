---
layout: post
title: Sort Colors II
date: 2015-10-21 14:38:05.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.</em></strong></p>


``` java
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

```
``` java
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
```
