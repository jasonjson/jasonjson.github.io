---
layout: post
title: Count and Say
date: 2015-10-21 02:16:28.000000000 -04:00
type: post
published: true
status: publish
categories:
- String
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466834470;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1407;}i:1;a:1:{s:2:"id";i:1789;}i:2;a:1:{s:2:"id";i:89;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>The count-and-say sequence is the sequence of integers beginning as follows:<br />
1, 11, 21, 1211, 111221, ...<br />
1 is read off as "one 1" or 11.<br />
11 is read off as "two 1s" or 21.<br />
21 is read off as "one 2, then one 1" or 1211.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param n the nth
     * @return the nth sequence
     */
    public String countAndSay(int n) {
        // Write your code here
        if(n == 0) return null;
        if(n == 1) return "1";
        StringBuilder str = new StringBuilder();
        String prev = countAndSay(n-1);
        //we build new string based on previous string
        char prev_char = prev.charAt(0);
        int start = 0;
        
        for(int i = 0; i < prev.length(); i++){
            if(prev.charAt(i) != prev_char){
                str.append(""+(i-start)+prev_char);
                //if the new char != previous char
                //we need to update count and char to new string
                start = i;
                prev_char = prev.charAt(i);
            }
        }
        //last char has no one to compare with, thus we need to add it mannully
        str.append("" + (prev.length() - start) + prev_char);
        return str.toString();
    }
}
</pre>
<p>[/expand]</p>
