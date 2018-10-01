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
public class Solution {
    public int longestValidParentheses(String s) {
        if (s == null || s.length() == 0) return 0;

        Stack<Integer> stack = new Stack<Integer>();
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

``` python
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        index = []
        start = ret = 0
        for i, c in enumerate(s):
            if c == "(":
                index.append(i)
            else:
                if not index:
                    start = i + 1
                else:
                    index.pop()
                    ret = max(ret, i - start + 1 if not index else i - index[-1])
        return ret
```
