---
layout: post
title: 20 - Valid parentheses
date: 2015-10-21 03:35:31.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.


``` java
public class Solution {
    /**
     * @param s A string
     * @return whether the string is a valid parentheses
     */
    public boolean isValidParentheses(String s) {
        if (s == null || s.length() == 0) return true;

        Stack<character> stack = new Stack<character>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (c == ')' || c == '}' || c == ']') {
                if (stack.isEmpty()) {
                    return false;//for the case s = "]", stack is empty
                } else {
                    char curr = stack.pop();
                    if ((curr == '(' && c != ')') || (curr == '{' && c != '}') || (curr == '[' && c != ']')) {
                        return false;
                    }
                }
            }
        }
        return stack.isEmpty();
    }
}
```

``` python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif c == ")" and stack.pop() != "(":
                return False
            elif c == "]" and stack.pop() != "[":
                return False
            elif c == "}" and stack.pop() != "{":
                return False
        return len(stack) == 0
```
