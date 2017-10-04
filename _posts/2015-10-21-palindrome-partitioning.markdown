---
layout: post
title: 131 - Palindrome Partitioning
date: 2015-10-21 03:25:53.000000000 -04:00
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
**Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.**


``` java
public class Solution {
    /**
     * @param s: A string
     * @return: A list of lists of string
     */
     //this kind of problem: find all subset, find the longest ... always using dfs and backtracking.
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<List<String>>();
        if (s == null || s.length() == 0) return result;

        List<String> list = new ArrayList<String>();

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
    public void partitionUtil(String s, List<List<String>> result, List<String> list) {
        if (s.length() == 0) {
            result.add(new ArrayList<String>(list));
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

``` python
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        if not s:
            return []

        ret = []
        self.helper(s, [], ret)
        return ret

    def helper(self, s, curr, ret):
        if len(s) == 0:
            ret.append(curr[:])
            return
        for i in xrange(len(s)):
            sub_s = s[0: i + 1]
            if self.is_pali(sub_s):
                curr.append(sub_s)
                self.helper(s[i + 1:], curr, ret)
                curr.pop()

    def is_pali(self, s):
        lo, hi = 0, len(s) - 1
        while lo <= hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True
```
