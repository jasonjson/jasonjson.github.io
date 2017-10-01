---
layout: post
title: Remove Invalid Parentheses
date: 2015-11-05 11:13:54.000000000 -05:00
tags:
- Leetcode
categories:
- BFS
- Brain Teaser
author: Jason
---
<p><strong><em>Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.</p>

Note: The input string may contain letters other than the parentheses ( and ).</em></strong></p>
``` java
public class Solution {
    public List<String> removeInvalidParentheses(String s) {
        List<String> result = new ArrayList<String>();
        if (s == null) return result;//s.length() == 0 is also a valid result
        
        Set<String> visited = new HashSet<String>();
        Queue<String> q = new LinkedList<String>();
        q.offer(s);
        visited.add(s);
        boolean found = false;
        while (!q.isEmpty()) {
            String curr = q.poll();
            if (isValid(curr)) {
                result.add(curr);
                found = true;
            }
            if (!found) {
                for (int i = 0; i < curr.length(); i++) {
                    if (curr.charAt(i) == '(' || curr.charAt(i) == ')') {
                        String newS = curr.substring(0, i) + curr.substring(i + 1);
                        if (!visited.contains(newS)) {
                            q.offer(newS);
                            visited.add(newS);
                        }
                    }
                }
            }
        }
        return result;
    }
    
    public boolean isValid(String s) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                count ++;
            }
            if (c == ')' && count -- == 0) {
                return false;
            }
        }
        return count == 0;
    }
}
```
