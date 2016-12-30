---
layout: post
title: Expression Evaluation
date: 2015-10-27 11:33:11.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Integer
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469286860;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:516;}i:1;a:1:{s:2:"id";i:970;}i:2;a:1:{s:2:"id";i:1409;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an expression string array, return the final result of this expression</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param expression: an array of strings;
     * @return: an integer
     */
    public int evaluateExpression(String[] expression) {
        // write your code here
        if (expression == null || expression.length == 0) return 0;
        Stack<integer> num = new Stack<integer>();
        Stack<string> op = new Stack<string>();
        
        for (String s : expression) {
            if (isOp(s)) {
                if (s.equals("(")) {
                    op.push(s);
                } else if (s.equals(")")) {
                    while (!op.peek().equals("(")) {
                        num.push(eval(num.pop(), num.pop(), op.pop()));
                    }
                    op.pop();
                } else {
                    while (!op.isEmpty() && order(s) <= order(op.peek())) {
                        num.push(eval(num.pop(), num.pop(), op.pop()));
                    }
                    op.push(s);
                }
            } else {
                num.push(Integer.parseInt(s));
            }
        }
        while (!op.isEmpty()) {
            num.push(eval(num.pop(), num.pop(), op.pop()));
        }
        if (!num.isEmpty()) {
            return num.pop();
        } else {
            return 0;
        }
    }
    public int eval(int n1, int n2, String operator) {
        if (operator.equals("+")) {
            return n2 + n1;
        } else if (operator.equals("-")) {
            return n2 - n1;
        } else if (operator.equals("/")) {
            return n2 / n1;
        } else {
            return n2 * n1;
        }
    }
    public boolean isOp(String s) {
        if (s.equals("+") || s.equals("-") || s.equals("*") || s.equals("/") || s.equals("(") || s.equals(")")) {
            return true;
        } else {
            return false;
        }
    }
    public int order(String s) {
        if (s.equals("*") || s.equals("/")) {
            return 2;
        } else if (s.equals("+") || s.equals("-")) {
            return 1;
        } else {
            return 0;
        }
    }
};
</string></string></integer></integer></pre>
<p>[/expand]</p>
