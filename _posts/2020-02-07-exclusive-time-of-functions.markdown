---
layout: post
title: 636 - Exclusive Time Of Functions
date: 2020-02-07
tags:
- Leetcode
categories:
- Array
author: Jason
---
On a single threaded CPU, we execute some functions.  Each function has a unique id between 0 and N-1. We store logs in timestamp order that describe when a function is entered or exited. Each log is a string with this format: "{function_id}:{"start" or "end"}:{timestamp}". For example, "0:start:3" means the function with id 0 started at the beginning of timestamp 3. "1:end:2" means the function with id 1 ended at the end of timestamp 2. A function's exclusive time is the number of units of time spent in this function.  Note that this does not include any recursive calls to child functions. The CPU is single threaded which means that only one function is being executed at a given time unit. Return the exclusive time of each function, sorted by their function id.

```python
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        prev_t = 0
        stack = []
        ret = [0] * n
        for log in logs:
            func_id, func, t = log.split(":")
            func_id, t = int(func_id), int(t)
            if func == "start":
                if stack:
                    ret[stack[-1]] += t - prev_t
                prev_t = t
                stack.append(func_id)
            else:
                ret[stack.pop()] += t - prev_t + 1
                prev_t = t + 1
        return ret
```
