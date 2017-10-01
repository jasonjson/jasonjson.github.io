---
layout: post
title: Detect Capital
date: 2017-05-04
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given a word, you need to judge whether the usage of capitals in it is right or not.  We define the usage of capitals in a word to be right when one of the following cases holds: All letters in this word are capitals, like "USA". All letters in this word are not capitals, like "leetcode". Only the first letter in this word is capital if it has more than one letter, like "Google". Otherwise, we define that this word doesn't use capitals in a right way.**

```python
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        first_upper = False
        all_upper = False
        rest_lower = True

        for i, char in enumerate(word):
            if i == 0 and char.isupper():
                first_upper = True
                all_upper = True
                continue

            if char.isupper():
                rest_lower = False
                if not first_upper or not all_upper:
                    return False
            else:
                all_upper = False
        return all_upper or rest_lower
```

```python
def detectCapitalUse(self, word):
    return word.isupper() or word.islower() or word.istitle()
```
