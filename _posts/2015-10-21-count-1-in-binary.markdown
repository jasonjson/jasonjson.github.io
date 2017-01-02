---
layout: post
title: Count 1 in Binary
date: 2015-10-21 02:38:23.000000000 -04:00
categories:
- Bit
author: Jason
---
<p><strong><em>Count how many 1 in binary representation of a 32-bit integer. follow up: Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).</em></strong></p>

<p><a href="http://www.java-samples.com/showtutorial.php?tutorialid=60">unsigned right shift</a><br />

``` java
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
```

``` java
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
```
