---
layout: post
title: 199 - Binary Tree Right Side View
date: 2015-11-04 15:49:10.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.**


``` java
public class Solution { //level order traversal
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if (root == null) return result;

        Queue<treenode> q = new LinkedList<treenode>();
        q.offer(root);
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode curr = q.poll();
                if (i == size - 1) {
                    result.add(curr.val);
                }
                if (curr.left != null) q.offer(curr.left);
                if (curr.right != null) q.offer(curr.right);
            }
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []
        prev, ret = [root], []
        while prev:
            curr = []
            ret.append(prev[-1].val)
            for node in prev:
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            prev = curr
        return ret
```
