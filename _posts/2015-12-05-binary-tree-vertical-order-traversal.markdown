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
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        index_map = collections.defaultdict(list)
        dist_map = {}
        queue = collections.deque([root])
        dist_map[root] = 0
        min_index = 2 ** 31 - 1
        while queue:
            curr = queue.popleft()
            index = dist_map.get(curr)
            min_index = min(min_index, index)
            index_map[index].append(curr.val)
            if curr.left:
                queue.append(curr.left)
                dist_map[curr.left] = index - 1
            if curr.right:
                queue.append(curr.right)
                dist_map[curr.right] = index + 1

        ret = []
        while min_index in index_map:
            ret.append(index_map[min_index])
            min_index += 1
        return ret
```
