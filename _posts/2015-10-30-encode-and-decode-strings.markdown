---
layout: post
title: 271 - Encode and Decode Strings
date: 2015-10-30 11:43:26.000000000 -04:00
tags:
- Leetcode
categories:
- String
author: Jason
---
**Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.**


``` python
class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "".join(str(len(s)) + "#" + s for s in strs)


    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if not s:
            return []

        i = 0
        ret = []
        while i < len(s):
            index = s.index("#", i)
            s_len = int(s[i:index])
            ret.append(s[index + 1 : index + s_len + 1])
            i = index + s_len + 1
        return ret
```
