---
layout: post
title: Flip Game II
date: 2015-10-29 11:49:37.000000000 -04:00
tags: algorithm
categories:
- DFS Backtracking
author: Jason
---
<p><strong><em>You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner. Write a function to determine if the starting player can guarantee a win.</em></strong></p>


``` java
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
```
