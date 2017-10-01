---
layout: post
title: Remove Duplicate Letters
date: 2015-12-09 12:59:38.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
<p><strong><em>Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.</em></strong></p>


``` java
public class Solution {
    public String removeDuplicateLetters(String s) {
        if (s == null || s.length() == 0) return "";
        
        int[] counts = new int[26];
        Stack<character> stack = new Stack<character>();
        for (char c : s.toCharArray()) {
            counts[c - 'a'] ++;
        }
        for (char c : s.toCharArray()) {
            counts[c - 'a'] --;
            if (stack.contains(c)) {
                continue;
            }
            while (!stack.isEmpty() && stack.peek() >= c && counts[stack.peek() - 'a'] > 0) {
                stack.pop();
            }
            stack.push(c);
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        return sb.reverse().toString();
    }
}
```
``` java
public class Solution {
    //Given the string s, the greedy choice (i.e., the leftmost letter in the answer) 
    //is the smallest suffix s[i .. ] contains all the unique letters.
    //怎么挑第一个字母？先找到最小的包含所有unique letters的前缀，例如"cbacdcbc",最小的前缀是"cba",
    //第一个字母必须从这其中挑，因为后面的字符串不包含a了。在这个前缀里挑最小的字母，就是'a'，然后
    //移除a前面所有的字母，并去掉后面所有的a。
    public String removeDuplicateLetters(String s) {
        if (s == null || s.length() == 0) return "";
        
        int[] counts = new int[26];
        boolean[] candidates = new boolean[26];
        for (char c : s.toCharArray()) {
            counts[c - 'a'] ++;
        }
        for (char c : s.toCharArray()) {
            candidates[c - 'a'] = true;
            if (--counts[c - 'a'] == 0) {
                break;
            }
        }
        for (char c = 'a'; c <= 'z'; c ++) {
            if (candidates[c - 'a']) {
                for (int i = 0; i < s.length(); i++) {
                    if (s.charAt(i) == c) {
                        return c + removeDuplicateLetters(s.substring(i+1).replaceAll("" + c, ""));
                    }
                }
            }
        }
        return "";
    }
}
```
