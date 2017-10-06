---
layout: post
title: 151 - Reverse Words in a String
date: 2015-10-21 02:13:20.000000000 -04:00
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given an input string, reverse the string word by word.**


``` java
public class Solution {
    /**
     * @param s : A string
     * @return : A string
     */
    public String reverseWords(String s) {
        // write your code
        if(s == null || s.length() == 0) return s;
        String[] arr = s.split(" ");
        //split the original string to str array, use space as separator, there will be empty strings in the array
        StringBuilder str = new StringBuilder();
        for(int i = arr.length-1; i >= 0; i--){
            if(!arr[i].equals("")){
            //!!!important, use "" instead of " " to deal with empty strings, not space
                str.append(arr[i]).append(" ");
            }
        }
        return str.toString();
    }
}
```

``` python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return " ".join(reversed([word for word in s.strip().split(" ") if word]))
```
