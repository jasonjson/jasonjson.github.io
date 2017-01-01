---
layout: post
title: Flip Game II
date: 2015-10-29 11:49:37.000000000 -04:00
type: post
published: true
status: publish
categories:
- DFS Backtracking
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463425514;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1150;}i:1;a:1:{s:2:"id";i:307;}i:2;a:1:{s:2:"id";i:1304;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner. Write a function to determine if the starting player can guarantee a win.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public boolean canWin(String s) {
        if (s == null || s.length() == 0) return false;
        
        List<string> path = new ArrayList<string>();
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == '+' && s.charAt(i-1) == '+') {
                String newS = s.substring(0, i-1) +"--"+s.substring(i+1);
                path.add(newS);
            }
        }
        for (String str : path) {
            if (!canWin(str)) {
                return true;
            }
        }
        return false;
    }
}
</string></string></pre>
<p>[/expand]</p>
