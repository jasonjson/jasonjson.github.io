---
layout: post
title: Strobogrammatic Number II
date: 2015-11-02 11:43:03.000000000 -05:00
tags:
- Algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down). Find all strobogrammatic numbers that are of length = n.</em></strong></p>


``` java
public class Solution {
    public List<string> findStrobogrammatic(int n) {
        return helper(n, n);
    }
    
    public List<string> helper(int n, int m) {
        if (n == 0) return new ArrayList<string>(Arrays.asList(""));
        if (n == 1) return new ArrayList<string>(Arrays.asList("0", "1", "8"));
        List<string> prev = helper(n - 2, m); //like count and say
        List<string> result = new ArrayList<string>();
        for (int i = 0; i < prev.size(); i++) {
            String s = prev.get(i);
            if (n != m) {
                result.add("0" + s + "0");//0 can't be the first number
            }
            result.add("1" + s + "1");
            result.add("8" + s + "8");
            result.add("6" + s + "9");
            result.add("9" + s + "6");
        }
        return result;
    }
}
```
