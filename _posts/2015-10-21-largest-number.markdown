---
layout: post
title: Largest Number
date: 2015-10-21 14:24:22.000000000 -04:00
categories:
- Brain teaser
- Integer
author: Jason
---
<p><strong><em>Given a list of non negative integers, arrange them such that they form the largest number.</em></strong></p>

``` java
public class Solution {
    /**
     *@param num: A list of non negative integers
     *@return: A string
     */
    public String largestNumber(int[] num) {
        // write your code here
        if (num == null || num.length == 0) return "";
        
        List<string> list = new ArrayList<string>();
        for (int n : num) {
            list.add(String.valueOf(n));
        }        
        Collections.sort(list, new Comparator<string>() {
            public int compare (String a, String b) {
                return (b + a).compareTo(a + b);
            }
        });
        StringBuilder sb = new StringBuilder();
        for (String s : list) {
            sb.append(s);
        }
        if (sb.charAt(0) == '0') {
            return "0";
        } else {
            return sb.toString();
        }
    }
}
```
