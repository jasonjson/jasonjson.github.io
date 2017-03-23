---
layout: post
title: Palindrome Partitioning
date: 2015-10-21 03:25:53.000000000 -04:00
tags:
- Algorithm
categories:
- DFS Backtracking
- Palindrome
author: Jason
---
<p><strong><em>Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.</em></strong></p>


``` java
public class Solution {
    /**
     * @param s: A string
     * @return: A list of lists of string
     */
     //this kind of problem: find all subset, find the longest ... always using dfs and backtracking.
    public List<List<string>> partition(String s) {
        List<List<string>> result = new ArrayList<List<string>>();
        if (s == null || s.length() == 0) return result;
        
        List<string> list = new ArrayList<string>();
        
        partitionUtil(s, result, list);
        return result;
    }    
    public boolean isPali(String s) {
        int lo = 0, hi = s.length() - 1;
        while (lo <= hi) {
            if (s.charAt(lo) != s.charAt(hi)) {
                return false;
            }
            lo ++;
            hi --;//bug forget this
        }
        return true;
    }    
    public void partitionUtil(String s, List<List<string>> result, List<string> list) {
        if (s.length() == 0) {
            result.add(new ArrayList<string>(list));
        }        
        for (int i = 1; i <= s.length(); i++) {
            String str = s.substring(0, i);
            if (isPali(str)) {
                list.add(str);
                String rest = s.substring(i);
                partitionUtil(rest, result, list);
                list.remove(list.size() - 1);//!!!dont forget
            }
        }
    }
}
```
