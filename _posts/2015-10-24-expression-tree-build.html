---
layout: post
title: Expression Tree Build
date: 2015-10-24 14:05:56.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463840242;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:509;}i:1;a:1:{s:2:"id";i:1409;}i:2;a:1:{s:2:"id";i:1071;}}}}
  _wpas_done_all: '1'
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>The structure of Expression Tree is a binary tree to evaluate certain expressions. All leaves of the Expression Tree have an number string value. All non-leaves of the Expression Tree have an operator string value. Now, given an expression array, build the expression tree of this expression, return the root of this expression tree.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param expression: A string array
     * @return: The root of expression tree
     */
    public ExpressionTreeNode build(String[] expression) {
        // write your code here
        if (expression == null || expression.length == 0) return null;
        Stack<expressiontreenode> operator = new Stack<expressiontreenode>();
        Stack<expressiontreenode> number = new Stack<expressiontreenode>();
        ExpressionTreeNode root = null;
        for (String s : expression) {
            ExpressionTreeNode node = new ExpressionTreeNode(s);
            if (isOp(s)) {
                if (s.equals("(")) {
                    operator.push(node);
                } else if (s.equals(")")) {
                    while (!operator.peek().symbol.equals("(")) {
                        root = operator.pop();
                        root.right = number.pop();
                        root.left = number.pop();
                        number.push(root);
                    }
                    operator.pop();
                } else {
                    while (!operator.isEmpty() && order(s) <= order(operator.peek().symbol)) {
                        root = operator.pop();
                        root.right = number.pop();
                        root.left = number.pop();
                        number.push(root);
                    }
                    operator.push(node);
                }
            } else {
                number.push(node);
            }
        }
        while (!operator.isEmpty()) {
            root = operator.pop();
            root.right = number.pop();
            root.left = number.pop();
            number.push(root);
        }
        if (!number.isEmpty()) {
            return number.pop();
        } else {
            return null;
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
}
</expressiontreenode></expressiontreenode></expressiontreenode></expressiontreenode></pre>
<p>[/expand]</p>
