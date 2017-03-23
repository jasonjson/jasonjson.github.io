---
layout: post
title: Binary Tree Vertical Order Traversal
date: 2015-12-05 09:53:04.000000000 -05:00
tags:
- Algorithm
categories:
- BFS
- Brain teaser
author: Jason
---
<p><strong><em>Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column). If two nodes are in the same row and column, the order should be from left to right.</em></strong></p>


``` java
public class Solution {
    public static List<List<integer>> verticalOrder(TreeNode root) {
        List<List<integer>> result = new ArrayList<List<integer>>();
        if (root == null) return result;

        HashMap<TreeNode, Integer> dist = new HashMap<TreeNode, Integer>();
        HashMap<Integer, List<integer>> map = new HashMap<>();
        Queue<treenode> q = new LinkedList<treenode>();
        q.offer(root);
        dist.put(root, 0);
        int minIndex = Integer.MAX_VALUE;
        while (!q.isEmpty()) {
            root = q.poll();
            int index = dist.get(root);
            minIndex = Math.min(minIndex, index);
            List<integer> list = map.containsKey(index) ?  map.get(index) : new ArrayList<>();
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
