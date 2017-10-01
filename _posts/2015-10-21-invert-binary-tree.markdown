---
layout: post
title: Invert Binary Tree
date: 2015-10-21 02:53:24.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Invert a binary tree**

``` java
public class Solution {
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void invertBinaryTree(TreeNode root) {
        // write your code here
        if (root == null) return;
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        //from top to bottom
        invertBinaryTree(root.left);
        invertBinaryTree(root.right);
    }
}
```

``` java
public class Solution {
    //iterative
    public void invertBinaryTree(TreeNode root) {
        // write your code here
        if (root == null) return;
        Stack<treenode> stack = new Stack<treenode>();

        stack.push(root);
        while (!stack.isEmpty()) {
            //we don't care if the current level is finished, when i level is finished, it goes automatically to i + 1 level, root remain the same, because it's already swapped in the above level
            TreeNode curr = stack.pop();
            TreeNode temp = curr.left;
            curr.left = curr.right;
            curr.right = temp;
            if (curr.left != null)  stack.push(curr.left);
            if (curr.right != null) stack.push(curr.right);
        }
    }
}
```

```python
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        stack = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return root
```

```python
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```
