---
layout: post
title: 489 - Robot Room Cleaner
date: 2020-02-04
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
Given a robot cleaner in a room modeled as a grid. Each cell in the grid can be empty or blocked. The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees. When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell. Design an algorithm to clean the entire room using only the 4 given APIs shown below.

```python
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        path = set()
        def dfs(x, y, dx, dy):
            robot.clean()
            path.add((x, y))

            for _ in range(4):
                if (x + dx, y + dy) not in path and robot.move():
                    dfs(x + dx, y + dy, dx, dy)

                robot.turnLeft()
                dx, dy = -dy, dx

            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()

        dfs(0, 0, 0, 1)
```
