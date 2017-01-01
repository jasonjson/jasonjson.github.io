---
layout: post
title: Basic Calculator II
date: 2015-11-03 14:05:09.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469040134;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1286;}i:1;a:1:{s:2:"id";i:1119;}i:2;a:1:{s:2:"id";i:1071;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Implement a basic calculator to evaluate a simple expression string.<br />
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.<br />
You may assume that the given expression is always valid.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
