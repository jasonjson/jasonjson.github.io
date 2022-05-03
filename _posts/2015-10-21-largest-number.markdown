---
layout: post
title: 179 - Largest Number
date: 2015-10-21 14:24:22.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a list of non negative integers, arrange them such that they form the largest number.**


``` java
public class Solution {
    /**
     *@param num: A list of non negative integers
     *@return: A string
     */
    public String largestNumber(int[] num) {
        // write your code here
        if (num == null || num.length == 0) return "";

        List<String> list = new ArrayList<String>();
        for (int n : num) {
            list.add(String.valueOf(n));
        }
        Collections.sort(list, new Comparator<String>() {
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

``` python
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            if a + b > b + a:
                return 1
            elif a + b < b + a:
                return -1
            else:
                return 0

        nums = [str(n) for n in nums]
        nums = sorted(nums, key=cmp_to_key(compare), reverse=True)
        return "".join(nums).lstrip("0") or "0"
```
