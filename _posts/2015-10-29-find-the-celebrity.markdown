---
layout: post
title: Find the Celebrity
date: 2015-10-29 14:57:47.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468660927;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1234;}i:1;a:1:{s:2:"id";i:1038;}i:2;a:1:{s:2:"id";i:1136;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them. Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense). You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution extends Relation {
    public int findCelebrity(int n) {
        if (n <= 0) return -1;
        if (n == 1) return 0;
        
        Stack<integer> stack = new Stack<integer>();
        for (int i = 0; i < n; i++) {
            stack.push(i);
        }
        while (stack.size() > 1) {
            int a = stack.pop(), b = stack.pop();
            if (knows(a, b)) {
                stack.push(b);
            } else {
                stack.push(a);
            }
        }
        //double check
        int c = stack.pop();
        for (int i = 0; i < n; i++) {
            if (i != c && (knows(c, i) || !knows(i, c))) {
                //if c knows anyone or anyone doesn't know c, return -1
                return -1;
            }
        }
        return c;
    }
}
</integer></integer></pre>
<p>[/expand]</p>
