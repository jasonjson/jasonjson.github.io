---
layout: post
title: Longest Valid Parentheses
date: 2015-11-15 10:28:38.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465433194;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:317;}i:1;a:1:{s:2:"id";i:1286;}i:2;a:1:{s:2:"id";i:1382;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.<br />
For "(()", the longest valid parentheses substring is "()", which has length = 2.<br />
Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
//和 maximum histogram 非常类似
public class Solution {
    public int longestValidParentheses(String s) {
        if (s == null || s.length() == 0) return 0;
        
        Stack<integer> stack = new Stack<integer>();//换换思维,不是push char而是push index便于求长度
        int start = 0, len = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(i);
            } else {
                if (stack.isEmpty()) {
                    start = i + 1;
                } else {
                    stack.pop();
                    len = Math.max(len, stack.isEmpty() ? i - start + 1 : i - stack.peek());
                }
            }
        }
        return len;
    }
}
</integer></integer></pre>
<p>[/expand]</p>
<p>[expand title = "TLE"]</p>
<pre>
public class Solution {
    public int longestValidParentheses(String s) {
        if (s == null || s.length() == 0) return 0;
        
        Set<string> visited = new HashSet<string>();
        Queue<string> q = new LinkedList<string>();
        q.offer(s);
        visited.add(s);
        while (!q.isEmpty()) {
            s = q.poll();
            if (isValid(s)) {
                return s.length();
            } else {
                for (int i = 0; i < s.length(); i++) {
                    String newS = s.substring(0, i) + s.substring(i + 1);
                    if (visited.add(newS)) {
                        q.offer(newS);
                    }
                }
            }
        }
        return 0;
    }
    
    public boolean isValid(String s) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                count ++;    
            } else {
                if (count <= 0) {
                    return false;
                } else {
                    count--;
                }
            }
        }
        return true;
    }
}
</string></string></string></string></pre>
<p>[/expand]</p>
