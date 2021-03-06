---
layout: post
title: 224 - Basic Calculator
date: 2015-11-03 13:49:17.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Implement a basic calculator to evaluate a simple expression string. The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces. You may assume that the given expression is always valid.**


``` java
public class Solution {
    //Simple iterative solution by identifying characters one by one. One important thing is that the input is valid, which means the parentheses are always paired and in order. Only 5 possible input we need to pay attention:digit: it should be one digit from the current number
    //'+': number is over, we can add the previous number and start a new number
    //'-': same as above
    //'(': push the previous result and the sign into the stack, set result to 0, just calculate the new result within the parenthesis.
    //')': pop out the top two numbers from stack, first one is the sign before this pair of parenthesis, second is the temporary result before this pair of parenthesis. We add them together.
    public int calculate(String s) {
        if (s == null || s.length() == 0) return -1;
        Stack<Integer> stack = new Stack<Integer>();

        int number = 0, sign = 1, result = 0;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                number = number * 10 + c - '0';//char不能用Integer.parseInt, 只能String用
            } else if (c == '+') {
                result += sign * number;
                number = 0;
                sign = 1;
            } else if (c == '-') {
                result += sign * number;
                number = 0;
                sign = -1;
            } else if (c == '(') {
                stack.push(result);//储存前面的计算结果
                stack.push(sign);
                sign = 1;
                result = 0;
            } else if (c == ')') {
                result += sign * number; //先把括号里的处理完
                number = 0;
                result *= stack.pop();//把处理括号前存在stack里的数据取出
                result += stack.pop();
            }
        }
        if (number != 0) result += sign * number;
        return result;
    }
}
```

``` python
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        stack = []
        num = ret = 0
        sign = 1
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "+":
                ret += sign * num
                num = 0
                sign = 1
            elif char == "-":
                ret += sign * num
                num = 0
                sign = -1
            elif char == "(":
                stack.append(ret)
                stack.append(sign)
                ret = 0
                sign = 1
            elif char == ")":
                ret += sign * num
                num = 0
                ret *= stack.pop()
                ret += stack.pop()
        if num:
            ret += sign * num
        return ret
```
