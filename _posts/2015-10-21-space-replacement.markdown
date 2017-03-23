---
layout: post
title: Space Replacement
date: 2015-10-21 02:14:50.000000000 -04:00
tags:
- Algorithm
categories:
- String
author: Jason
---
<p><strong><em>Write a method to replace all spaces in a string with \%20. The string is given in a characters array, you can assume it has enough space for replacement and you are given the true length of the string.</em></strong></p>


``` java
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
```
