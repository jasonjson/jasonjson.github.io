---
layout: post
title: 227 - Basic Calculator II
date: 2020-01-09
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Implement a basic calculator to evaluate a simple expression string.  The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero. You may assume that the given expression is always valid.**


``` java
public class Solution {
    public int calculate(String s) {
        if (s == null || s.length() == 0) return -1;

        int result = 0, sign = 1, num = 0, prev = 0, opt = 0;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {//number
                num = num * 10 + c - '0';//相当于prevNum
            } else if (c != ' ') {//要排除空字符，跟basic calculator的if语句有区别
                if (opt == 1) {
                    num = prev * num;
                } else if (opt == -1) {
                    num = prev / num;
                }
                opt = 0;//清空opt
                if (c == '+') {
                    result += sign * num;//处理加号前面的运算
                    sign = 1;
                } else if (c == '-') {
                    result += sign * num;
                    sign = -1;
                } else if (c == '*') {
                    prev = num;//不能更新result，只能存下值来 等找到下个num再用
                    opt = 1;
                } else if (c == '/') {
                    prev = num;
                    opt = -1;
                }
                num = 0;//清空num,因为已经被用过了
            }
        }
        if (num != 0) {
            if (opt == 1) {
                result += sign * prev * num;//相当于把前面num = prev * num;result += num * sign;并到一起
            } else if (opt == -1) {
                result += sign * prev / num;
            } else {
                result += sign * num;
            }
        }
        return result;
    }
}
```

``` python
class Solution:
    def calculate(self, s: str) -> int:
        num_stack = []
        sign = "+"
        num = 0
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if c in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    num_stack.append(num)
                elif sign == "-":
                    num_stack.append(-num)
                elif sign == '*':
                    num_stack.append(num_stack.pop() * num)
                elif sign == '/':
                    num_stack.append(int(num_stack.pop() / num))
                sign = c
                num = 0
        return sum(num_stack)
```
