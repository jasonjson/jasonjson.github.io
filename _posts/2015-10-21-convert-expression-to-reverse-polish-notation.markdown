---
layout: post
title: Convert Expression to Reverse Polish Notation
date: 2015-10-21 14:12:54.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
- Data Structure
author: Jason
---
``` java
public class Solution {
    public ArrayList<String> convertToRPN(String[] expression) {
        ArrayList<String> result = new ArrayList<String>();
        if (expression == null || expression.length == 0) return result;        
        Stack<String> stack = new Stack<String>();
        for (String s : expression) {
            if (isOp(s)) {
                if (s.equals("(")) {
                    stack.push(s);
                } else if (s.equals(")")) {
                    while (!stack.isEmpty()) {
                        String p = stack.pop();
                        if (p.equals("(")) {
                            break;
                        }
                        result.add(p);
                    }
                } else {
                    while (!stack.isEmpty() && order(s) <= order(stack.peek())) {// <= not < 因为如果s与stack.peek()相同order的话，我们要先处理栈里的，因为栈里的operator在表达式左边. 注意区分从左边开始处理和从右边开始处理 此处的<和<=
                        result.add(stack.pop());
                    }
                    stack.push(s);
                }
            } else {
                result.add(s);
            }
        }
        while (!stack.isEmpty()) {
            result.add(stack.pop());
        }
        return result;
    }
    public boolean isOp(String str) {
        if (str.equals("+") || str.equals("-") || str.equals("*") || str.equals("/") || str.equals("(") || str.equals(")")) {
            return true;
        } else {
            return false;
        }
    }
    public int order(String str) {
        if (str.equals("*") || str.equals("/")) {
            return 2;
        } else if (str.equals("+") || str.equals("-")) {
            return 1;//must have
        } else {
            return 0;
        }
    }
}
```
