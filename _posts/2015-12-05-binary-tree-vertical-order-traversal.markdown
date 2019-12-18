---
layout: post
title: 314 - Binary Tree Vertical Order Traversal
date: 2015-12-05 09:53:04.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column). If two nodes are in the same row and column, the order should be from left to right.**


``` java
public class Solution {
    public static List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (root == null) return result;

        HashMap<TreeNode, Integer> dist = new HashMap<TreeNode, Integer>();
        HashMap<Integer, List<Integer>> map = new HashMap<>();
        Queue<treenode> q = new LinkedList<treenode>();
        q.offer(root);
        dist.put(root, 0);
        int minIndex = Integer.MAX_VALUE;
        while (!q.isEmpty()) {
            root = q.poll();
            int index = dist.get(root);
            minIndex = Math.min(minIndex, index);
            List<Integer> list = map.containsKey(index) ?  map.get(index) : new ArrayList<>();
            list.add(root.val);
            map.put(index, list);
            if (root.left != null) {
                q.offer(root.left);
                dist.put(root.left, index - 1);
            }
            if (root.right != null) {
                q.offer(root.right);
                dist.put(root.right, index + 1);
            }
        }
        while (map.containsKey(minIndex)) {
            result.add(map.get(minIndex++));
        }
        return result;
    }
}
```

``` python
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [(0, root)]
        level_map = defaultdict(list)
        while queue:
            level, curr = queue.pop(0)
            level_map[level].append(curr.val)
            if curr.left:
                queue.append((level - 1, curr.left))
            if curr.right:
                queue.append((level + 1, curr.right))
        ret = []
        for key in sorted(level_map):
            ret.append(level_map[key])
        return ret
```
