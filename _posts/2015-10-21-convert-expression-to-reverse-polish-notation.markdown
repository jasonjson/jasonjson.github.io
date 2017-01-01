---
layout: post
title: Convert Expression to Reverse Polish Notation
date: 2015-10-21 14:12:54.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Data Structure
tags: []
meta:
  _spost_short_title: ''
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468064125;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:516;}i:1;a:1:{s:2:"id";i:1789;}i:2;a:1:{s:2:"id";i:1071;}}}}
  _wpas_done_all: '1'
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public ArrayList<string> convertToRPN(String[] expression) {
        ArrayList<string> result = new ArrayList<string>();
        if (expression == null || expression.length == 0) return result;        
        Stack<string> stack = new Stack<string>();
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
</string></string></string></string></string></pre>
<p>[/expand]</p>
