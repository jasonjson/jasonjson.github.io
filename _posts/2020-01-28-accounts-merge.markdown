---
layout: post
title: 721 - Accounts Merge
date: 2020-01-28
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

```python
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union = {}
        parent_map = defaultdict(set)
        name_map = {}

        def find_union(node):
            if union.get(node, node) == node:
                union[node] = node
                return node
            else:
                return find_union(union[node])

        for name, *emails in accounts:
            parent = find_union(emails[0])
            for email in emails[1:]:
                p = find_union(email)
                union[p] = parent

        for name, *emails in accounts:
            for email in emails:
                parent = find_union(email)
                parent_map[parent].add(email)
                name_map[parent] = name

        ret = []
        for parent, name in name_map.items():
            ret.append([name] + sorted(list(parent_map[parent])))
        return ret
```
