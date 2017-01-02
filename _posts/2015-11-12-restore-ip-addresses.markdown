---
layout: post
title: Restore IP Addresses
date: 2015-11-12 09:09:28.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given a string containing only digits, restore it by returning all possible valid IP address combinations.</em></strong></p>


``` java
public class Solution {
    public List<string> restoreIpAddresses(String s) {
        List<string> result = new ArrayList<string>();
        if (s == null || s.length() == 0) return result;
        
        helper(s, 0, "", result);
        return result;
    }
    
    public void helper(String s, int step, String path, List<string> result) {
        if (step == 4) {//这个负责控制多少段字符
            if (s.length() == 0) {
                result.add(path.substring(0, path.length() - 1));
            }
            return;
//不能合并上面的if，当step == 4就不必往下继续了, 也不能调换顺序，s可能很长，只要到了第四步就return
        }
        for (int i = 1; i <= 3; i++) {
           if (s.length() < i) return;
           int val = Integer.parseInt(s.substring(0, i));
           if (val <= 255 && String.valueOf(val).length() == i) {//去掉010这样的IP
               helper(s.substring(i), step + 1, path + val + ".", result);
           }
        }
    }
}
```
