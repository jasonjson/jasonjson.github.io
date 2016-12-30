---
layout: post
title: Different Ways to Add Parentheses
date: 2015-11-02 16:24:34.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469056906;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1302;}i:1;a:1:{s:2:"id";i:1414;}i:2;a:1:{s:2:"id";i:536;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public List<integer> diffWaysToCompute(String input) {
        if (input == null || input.length() == 0) return new ArrayList<integer>();
        
        List<string> path = new ArrayList<string>();
        for (int i = 0; i < input.length(); i++) {
            int j = i;
            while (j < input.length() && Character.isDigit(input.charAt(j))) {
                j++;//string has no such isDigit method
            }
            path.add(input.substring(i,j));
            if (j < input.length()) {
                path.add(input.substring(j, j + 1));
            }//i will increment in for loop, so no need to increment j here
            i = j;
        }//separate strings into numbers and operators
        return helper(path, 0, path.size() - 1);
    }
    
    public List<integer> helper(List<string> path, int lo, int hi) {
        List<integer> result = new ArrayList<integer>();
        if (lo == hi) {
            result.add(Integer.parseInt(path.get(lo)));//!!transfer to int
            return result;
        }
        for (int i = lo + 1; i <= hi - 1; i+=2) {
            String operator = path.get(i);
            List<integer> left = helper(path, lo, i - 1);//this is like unique binary search trees
            List<integer> right = helper(path, i + 1, hi);
            for (int m : left) {
                for (int n : right) {
                    if (operator.equals("+")) {
                        result.add(m + n);
                    } else if (operator.equals("-")) {
                        result.add(m - n);
                    } else {
                        result.add(m * n);
                    }
                }
            }
        }
        return result;
    }
}
</integer></integer></integer></integer></string></integer></string></string></integer></integer></pre>
<p>[/expand]</p>
