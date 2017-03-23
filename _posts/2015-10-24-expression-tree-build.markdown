---
layout: post
title: Expression Tree Build
date: 2015-10-24 14:05:56.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
- Data Structure
author: Jason
---
<p><strong><em>The structure of Expression Tree is a binary tree to evaluate certain expressions. All leaves of the Expression Tree have an number string value. All non-leaves of the Expression Tree have an operator string value. Now, given an expression array, build the expression tree of this expression, return the root of this expression tree.</em></strong></p>


``` java
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
```
