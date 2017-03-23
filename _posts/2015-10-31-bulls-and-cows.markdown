---
layout: post
title: Bulls and Cows
date: 2015-10-31 20:21:40.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
- String
author: Jason
---
<p><strong><em>You are playing the following Bulls and Cows game with your friend: You write a 4-digit secret number and ask your friend to guess it, each time your friend guesses a number, you give a hint, the hint tells your friend how many digits are in the correct positions (called "bulls") and how many digits are in the wrong positions (called "cows"), your friend will use those hints to find out the secret number.</em></strong></p>


``` java
public class Solution {
    public String getHint(String secret, String guess) {
        int bulls = 0, cows = 0;
        int[] digits = new int[10];
        for (int i = 0; i < secret.length(); i++) {
            if (secret.charAt(i) == guess.charAt(i)) {
                bulls ++;
            } else {
                if (digits[secret.charAt(i) - '0'] ++ < 0) cows++;
                //digits[secret.charAt(i) - '0'] < 0表明guess里一定出现过这个char所以才会是负值
                if (digits[guess.charAt(i) - '0'] -- > 0) cows++;
                //Increment cows when either number from secret was already seen in guess or vice versa.
            }
        }
        return bulls + "A" + cows + "B";
    }
}
```
