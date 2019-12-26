---
layout: post
title: 609 - Find Duplicate File In System
date: 2019-12-26
tags:
- Leetcode
categories:
- Array
author: Jason
---

```python
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        if not paths:
            return []

        content_dir = defaultdict(list)
        for path in paths:
            directory, *files = path.split()
            for f in files:
                filename, content = f.split("(")
                content_dir[content].append(directory + "/" + filename)
        return [v for v in content_dir.values() if len(v) > 1]
```
