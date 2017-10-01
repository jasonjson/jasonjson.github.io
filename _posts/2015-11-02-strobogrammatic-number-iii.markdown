---
layout: post
title: Strobogrammatic Number III
date: 2015-11-02 12:13:53.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
<p><strong><em>A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).</p>

Write a function to count the total strobogrammatic numbers that exist in the range of low &lt;= num &lt;= high.</p>
For example,</p>
Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.</em></strong></p>
``` java
public class Solution {
    public static int strobogrammaticInRange(String low, String high) {
        int len1 = low.length(), len2 = high.length();
        Set<String> set = new HashSet<String>();
        set.addAll(getNumber(len1, len1));
        set.addAll(getNumber(len2, len2));//must put in set, there can be duplicates in each list from len1 and len2, eg: len1 = len2
        int count = 0;
        for (String s : set) {
            if (Long.parseLong(s) >= Long.parseLong(low) && Long.parseLong(s) <= Long.parseLong(high)) {
                count++;
            }
        }
        for (int i = len1 + 1; i < len2; i++) {
            count += getCount(i);
        }
        return count;
    }

    public static List<String> getNumber(int n, int m) {
        if (n == 0) return new ArrayList<String>(Arrays.asList(""));
        if (n == 1) return new ArrayList<String>(Arrays.asList("1", "0", "8"));
        List<String> prev = getNumber(n - 2, m);
        List<String> result = new ArrayList<String>();
        for (int i = 0; i < prev.size(); i++) {
            String s = prev.get(i);
            if (n != m) {
                result.add("0" + s + "0");
            }
            result.add("1" + s + "1");
            result.add("8" + s + "8");
            result.add("6" + s + "9");
            result.add("9" + s + "6");
        }
        return result;
    }

    public static int getCount(int n) {
        if (n == 0) return 0;
        if (n % 2 == 0) {
            return 4 * (int)Math.pow(5, n / 2 - 1);
        } else {
            return 4 * (int)Math.pow(5, n / 2 - 1) * 3;
        }
    }
}
```
