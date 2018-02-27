---
layout: post
title: 359 - Logger Rate Limiter
date: 2018-02-27
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds. Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.**


```python
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.last_printed = {}


    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """

        if message not in self.last_printed:
            self.last_printed[message] = timestamp
            return True
        else:
            last_printed_time = self.last_printed[message]
            if timestamp - last_printed_time >= 10:
                self.last_printed[message] = timestamp
                return True
            else:
                return False
```
