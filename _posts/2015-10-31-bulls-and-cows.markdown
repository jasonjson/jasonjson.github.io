---
layout: post
title: 299 - Bulls and Cows
date: 2015-10-31 20:21:40.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**You are playing the following Bulls and Cows game with your friend: You write a 4-digit secret number and ask your friend to guess it, each time your friend guesses a number, you give a hint, the hint tells your friend how many digits are in the correct positions (called "bulls") and how many digits are in the wrong positions (called "cows"), your friend will use those hints to find out the secret number.**


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

``` python
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        digit_map = {}
        bull = cow = 0
        for s, g in zip(secret, guess):
            if s == g:
                bull += 1
            else:
                if digit_map.get(s, 0) < 0:
                    cow += 1
                if digit_map.get(g, 0) > 0:
                    cow += 1
                digit_map[s] = digit_map.get(s, 0) + 1
                digit_map[g] = digit_map.get(g, 0) - 1
        return str(bull) + "A" + str(cow) + "B"
```
