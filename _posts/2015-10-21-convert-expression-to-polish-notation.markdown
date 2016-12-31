---
layout: post
title: Convert Expression to Polish Notation
date: 2015-10-21 14:13:38.000000000 -04:00
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
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467197311;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:510;}i:1;a:1:{s:2:"id";i:509;}i:2;a:1:{s:2:"id";i:1409;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an expression string array, return the Polish notation of this expression. (remove the parentheses)</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public ArrayList<string> convertToPN(String[] expression) {
        ArrayList<string> result = new ArrayList<string>();
        if (expression == null || expression.length == 0) return result;
        Stack<string> stack = new Stack<string>();
        for (int i = expression.length - 1; i >= 0; i--) {
            String s = expression[i];
            if (isOp(s)) {
                if (s.equals(")")) {
                    stack.push(s);
                } else if (s.equals("(")) {
                    while (!stack.isEmpty() && !stack.peek().equals(")") {
                        result.add(stack.pop());
                    }
                    stack.pop();
                } else {
                    while (!stack.isEmpty() && order(s) < order(stack.peek())) {
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
        Collections.reverse(result);
        return result;
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
}
</string></string></string></string></string></pre>
<p>[/expand]</p>
