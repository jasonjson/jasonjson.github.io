---
layout: post
title: Space Replacement
date: 2015-10-21 02:14:50.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464086827;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1407;}i:1;a:1:{s:2:"id";i:89;}i:2;a:1:{s:2:"id";i:1890;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Write a method to replace all spaces in a string with \%20. The string is given in a characters array, you can assume it has enough space for replacement and you are given the true length of the string.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param string: An array of Char
     * @param length: The true length of the string
     * @return: The true length of new string
     */
    public int replaceBlank(char[] string, int length) {
        // Write your code here
        if(string == null || string.length == 0) return 0;
        int result = length;
        for(int i = 0; i < length; i++){
            if (string[i] == ' ') result += 2;
        }
        
        int index = result - 1;//we need to find the true length first!!
        for(int i = length - 1; i >= 0; i--){
            if(string[i] == ' '){
                string[index] = '0';
                string[index-1] = '2';
                string[index-2] = '%';
                index -= 3;
            }else{
                string[index] = string[i];
                index --;
            }
        }
        return result;
    }
}
</pre>
<p>[/expand]</p>
