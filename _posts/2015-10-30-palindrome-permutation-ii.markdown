---
layout: post
title: Palindrome Permutation II
date: 2015-10-30 16:14:52.000000000 -04:00
tags:
- Algorithm
categories:
- DFS Backtracking
- Palindrome
- Permutation
author: Jason
---
<p><strong><em>Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.</em></strong></p>


``` java
public class Solution {
    public List<string> generatePalindromes(String s) {
        List<string> result = new ArrayList<string>();
        if (s == null || s.length() == 0) return result;
        
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        List<character> list = new ArrayList<character>();
        String mid = "";
        for (char c : map.keySet()) {
            if (map.get(c) % 2 != 0) {
                mid += c;
            }
            for (int i = 0; i < map.get(c) / 2; i++) {
                list.add(c);
            }
        }
        if (mid.length() > 1) return result;//more than two elements with odd counts
        boolean[] visited = new boolean[list.size()];
        helper(list, mid, visited, new StringBuilder(), result);
        return result;
    }
    
    public void helper(List<character> list, String mid, boolean[] visited, StringBuilder sb, List<string> result) {
        if (sb.length() == list.size()) {
            result.add(sb.toString() + mid + sb.reverse().toString());
            sb.reverse();
            return;
        }
        for (int i = 0; i < list.size(); i++) {
            if (visited[i] || i > 0 && list.get(i) == list.get(i-1) && !visited[i-1]) {
                continue;//the way we add elements to the list makes sure the same elements are adjacent, no need to sort
            }
            sb.append(list.get(i));
            visited[i] = true;
            helper(list, mid, visited, sb, result);
            visited[i] = false;
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
```

``` java
public class Solution {
    public List<string> generatePalindromes(String s) {
       List<string> result = new ArrayList<string>();
       boolean[] visited = new boolean[s.length()];
       helper(s, "", visited, result);
       return result;
    }
    
    public void helper(String s, String path, boolean[] visited, List<string> result) {
        if (path.length() == s.length() && isPali(path)) {
            result.add(new String(path));
            return;
        }
        for (int i = 0; i < s.length(); i++) {
            if (visited[i] || (i > 0 && s.charAt(i) == s.charAt(i-1) && !visited[i-1])) {
                continue;
            }
            path += s.charAt(i);
            visited[i] = true;
            helper(s, path, visited, result);
            path = path.substring(0, path.length() - 1);
            visited[i] = false;
        }
    }
    
    public boolean isPali(String s) {
        int lo = 0, hi = s.length() - 1;
        while (lo <= hi) {
            if (s.charAt(lo) != s.charAt(hi)) {
                return false;
            }
            lo ++;
            hi --;
        }
        return true;
    }
}
```
