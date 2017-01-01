---
layout: post
title: Remove Invalid Parentheses
date: 2015-11-05 11:13:54.000000000 -05:00
type: post
published: true
status: publish
categories:
- BFS
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469122310;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:317;}i:1;a:1:{s:2:"id";i:438;}i:2;a:1:{s:2:"id";i:433;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.<br />
Note: The input string may contain letters other than the parentheses ( and ).</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public List<string> removeInvalidParentheses(String s) {
        List<string> result = new ArrayList<string>();
        if (s == null) return result;//s.length() == 0 is also a valid result
        
        Set<string> visited = new HashSet<string>();
        Queue<string> q = new LinkedList<string>();
        q.offer(s);
        visited.add(s);
        boolean found = false;
        while (!q.isEmpty()) {
            String curr = q.poll();
            if (isValid(curr)) {
                result.add(curr);
                found = true;
            }
            if (!found) {
                for (int i = 0; i < curr.length(); i++) {
                    if (curr.charAt(i) == '(' || curr.charAt(i) == ')') {
                        String newS = curr.substring(0, i) + curr.substring(i + 1);
                        if (!visited.contains(newS)) {
                            q.offer(newS);
                            visited.add(newS);
                        }
                    }
                }
            }
        }
        return result;
    }
    
    public boolean isValid(String s) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                count ++;
            }
            if (c == ')' && count -- == 0) {
                return false;
            }
        }
        return count == 0;
    }
}
</string></string></string></string></string></string></string></pre>
<p>[/expand]</p>
