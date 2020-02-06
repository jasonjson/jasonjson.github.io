---
layout: post
title: 889 - Construct Binary Tree From Preorder And Postorder Traversal
date: 2020-02-06
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
Return any binary tree that matches the given preorder and postorder traversals. Values in the traversals pre and post are distinct positive integers.

```python
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        stack = [TreeNode(pre[0])]
        j = 0
        for val in pre[1:]:
            while stack[-1].val == post[j]:
                stack.pop()
                j += 1
            node = TreeNode(val)
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
```
