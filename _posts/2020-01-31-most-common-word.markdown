---
layout: post
title: 819 - Most Common Word
date: 2020-01-31
tags:
- Leetcode
categories:
- String
author: Jason
---
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique. Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

```python
from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if not paragraph:
            return ""

        words = re.findall("\w+", paragraph.lower())
        counter = Counter(w for w in words if w not in banned)
        return max(counter.items(), key=lambda x: x[1])[0]
```
