---
layout: post
title: Basic Calculator
date: 2015-11-03 13:49:17.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463907307;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1290;}i:1;a:1:{s:2:"id";i:1357;}i:2;a:1:{s:2:"id";i:1512;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Implement a basic calculator to evaluate a simple expression string.<br />
The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .<br />
You may assume that the given expression is always valid.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    //Simple iterative solution by identifying characters one by one. One important thing is that the input is valid, which means the parentheses are always paired and in order. Only 5 possible input we need to pay attention:digit: it should be one digit from the current number
    //'+': number is over, we can add the previous number and start a new number
    //'-': same as above
    //'(': push the previous result and the sign into the stack, set result to 0, just calculate the new result within the parenthesis.
    //')': pop out the top two numbers from stack, first one is the sign before this pair of parenthesis, second is the temporary result before this pair of parenthesis. We add them together.
    public int calculate(String s) {
        if (s == null || s.length() == 0) return -1;
        Stack<integer> stack = new Stack<integer>();
        
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
</integer></integer></pre>
<p>[/expand]</p>
