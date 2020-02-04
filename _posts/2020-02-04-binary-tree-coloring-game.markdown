---
layout: post
title: 1145 - Binary Tree Coloring Game
date: 2020-02-04
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
Two players play a turn based game on a binary tree.  We are given the root of this binary tree, and the number of nodes n in the tree.  n is odd, and each node has a distinct value from 1 to n. Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x.  The first player colors the node with value x red, and the second player colors the node with value y blue. Then, the players take turns starting with the first player.  In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.) If (and only if) a player cannot choose such a node in this way, they must pass their turn.  If both players pass their turn, the game ends, and the winner is the player that colored more nodes. You are the second player.  If it is possible to choose such a y to ensure you win the game, return true.  If it is not possible, return false.

```python
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        c = [0, 0]
        def count(node):
            if not node:
                return 0
            left = count(node.left)
            right = count(node.right)
            if node.val == x:
                c[0], c[1] = left, right
            return left + right + 1

        return count(root) // 2 < max(max(c), n - sum(c) - 1)
```
