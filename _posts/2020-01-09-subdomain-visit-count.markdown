---
layout: post
title: 811 - Subdomain Visit Count
date: 2020-01-09
tags:
- Leetcode
categories:
- Array
author: Jason
---
**A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly. Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com". We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.**

```python
from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        if not cpdomains:
            return []

        count_map = defaultdict(int)
        for domain in cpdomains:
            count, *ds = domain.replace(" ", ".").split(".")
            for i in range(len(ds)):
                count_map[".".join(ds[i:])] += int(count)

        return [" ".join([str(v), k]) for k, v in count_map.items()]
```
