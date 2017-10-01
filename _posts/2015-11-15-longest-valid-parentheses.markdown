---
layout: post
title: 32 - Longest Valid Parentheses
date: 2015-11-15 10:28:38.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.**
* For "(()", the longest valid parentheses substring is "()", which has length = 2.
* Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.


``` java
//和 maximum histogram 非常类似
public class Solution {
    public int longestValidParentheses(String s) {
        if (s == null || s.length() == 0) return 0;

        Stack<Integer> stack = new Stack<Integer>();//换换思维,不是push char而是push index便于求长度
        int start = 0, len = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(i);
            } else {
                if (stack.isEmpty()) {
                    start = i + 1;
                } else {
                    stack.pop();
                    len = Math.max(len, stack.isEmpty() ? i - start + 1 : i - stack.peek());
                }
            }
        }
        return len;
    }
}
```
``` java
public class Solution {
    public int longestValidParentheses(String s) {
        if (s == null || s.length() == 0) return 0;

        Set<String> visited = new HashSet<String>();
        Queue<String> q = new LinkedList<String>();
        q.offer(s);
        visited.add(s);
        while (!q.isEmpty()) {
            s = q.poll();
            if (isValid(s)) {
                return s.length();
            } else {
                for (int i = 0; i < s.length(); i++) {
                    String newS = s.substring(0, i) + s.substring(i + 1);
                    if (visited.add(newS)) {
                        q.offer(newS);
                    }
                }
            }
        }
        return 0;
    }

    public boolean isValid(String s) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                count ++;
            } else {
                if (count <= 0) {
                    return false;
                } else {
                    count--;
                }
            }
        }
        return true;
    }
}
```
