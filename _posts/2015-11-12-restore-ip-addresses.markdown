---
layout: post
title: Restore IP Addresses
date: 2015-11-12 09:09:28.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467716307;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1414;}i:1;a:1:{s:2:"id";i:1208;}i:2;a:1:{s:2:"id";i:1196;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a string containing only digits, restore it by returning all possible valid IP address combinations.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public List<string> restoreIpAddresses(String s) {
        List<string> result = new ArrayList<string>();
        if (s == null || s.length() == 0) return result;
        
        helper(s, 0, "", result);
        return result;
    }
    
    public void helper(String s, int step, String path, List<string> result) {
        if (step == 4) {//这个负责控制多少段字符
            if (s.length() == 0) {
                result.add(path.substring(0, path.length() - 1));
            }
            return;
//不能合并上面的if，当step == 4就不必往下继续了, 也不能调换顺序，s可能很长，只要到了第四步就return
        }
        for (int i = 1; i <= 3; i++) {
           if (s.length() < i) return;
           int val = Integer.parseInt(s.substring(0, i));
           if (val <= 255 && String.valueOf(val).length() == i) {//去掉010这样的IP
               helper(s.substring(i), step + 1, path + val + ".", result);
           }
        }
    }
}
</string></string></string></string></pre>
<p>[/expand]</p>
