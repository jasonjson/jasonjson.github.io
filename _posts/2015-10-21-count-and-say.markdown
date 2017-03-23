---
layout: post
title: Count and Say
date: 2015-10-21 02:16:28.000000000 -04:00
tags:
- Algorithm
categories:
- String
author: Jason
---
<p><strong><em>The count-and-say sequence is the sequence of integers beginning as follows:</p>

1, 11, 21, 1211, 111221, ...</p>
1 is read off as "one 1" or 11.</p>
11 is read off as "two 1s" or 21.</p>
21 is read off as "one 2, then one 1" or 1211.</em></strong></p>

``` java
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
```
