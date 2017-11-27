---
layout: post
title: Pick a random number from a BST
date: 2016-01-09 10:40:16.000000000 -05:00
tags:
- OA
categories:
- Brain Teaser
author: Jason
---
**Randomly pick a number from binary searach tree**


``` java
public class Solution {
    public static int pickRandom(TreeNode root) {
        if (root == null) return -1;

        List<Integer> nums = getList(root);
        return nums.get(rand.nextInt(nums.size()));
    }

    public static List<Integer> getList(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;

        List<Integer> left = getList(root.left);
        List<Integer> right = getList(root.right);
        result.addAll(left);
        result.add(root.val);
        result.addAll(right);
        return result;
    }
}
```

``` python
class Solution(object):
    def pickRandom(self, root):
        if not root:
            return

        stack, ret = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                ret.append(root)
                root = root.right
        return ret[random.randInt(0, len(ret) - 1)]
```
